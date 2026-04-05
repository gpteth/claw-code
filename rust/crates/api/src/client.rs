use crate::error::ApiError;
use crate::providers::claw_provider::{self, AuthSource, ClawApiClient};
use crate::providers::openai_compat::{self, OpenAiCompatClient, OpenAiCompatConfig};
use crate::providers::{self, Provider, ProviderKind};
use crate::types::{MessageRequest, MessageResponse, StreamEvent};

async fn send_via_provider<P: Provider>(
    provider: &P,
    request: &MessageRequest,
) -> Result<MessageResponse, ApiError> {
    provider.send_message(request).await
}

async fn stream_via_provider<P: Provider>(
    provider: &P,
    request: &MessageRequest,
) -> Result<P::Stream, ApiError> {
    provider.stream_message(request).await
}

#[derive(Debug, Clone)]
pub enum ProviderClient {
    ClawApi(ClawApiClient),
    Xai(OpenAiCompatClient),
    OpenAi(OpenAiCompatClient),
    OpenRouter(OpenAiCompatClient),
}

impl ProviderClient {
    pub fn from_model(model: &str) -> Result<Self, ApiError> {
        Self::from_model_with_default_auth(model, None)
    }

    pub fn from_model_with_default_auth(
        model: &str,
        default_auth: Option<AuthSource>,
    ) -> Result<Self, ApiError> {
        // If CLAW_GATEWAY_URL is set, route all requests through the gateway.
        // This allows the CLI to use the gateway as a managed proxy.
        if let Some(gateway) = Self::gateway_client() {
            return Ok(gateway);
        }

        let resolved_model = providers::resolve_model_alias(model);
        match providers::detect_provider_kind(&resolved_model) {
            ProviderKind::ClawApi => Ok(Self::ClawApi(match default_auth {
                Some(auth) => ClawApiClient::from_auth(auth),
                None => ClawApiClient::from_env()?,
            })),
            ProviderKind::Xai => Ok(Self::Xai(OpenAiCompatClient::from_env(
                OpenAiCompatConfig::xai(),
            )?)),
            ProviderKind::OpenAi => Ok(Self::OpenAi(OpenAiCompatClient::from_env(
                OpenAiCompatConfig::openai(),
            )?)),
            ProviderKind::OpenRouter => Ok(Self::OpenRouter(OpenAiCompatClient::from_env(
                OpenAiCompatConfig::openrouter(),
            )?)),
        }
    }

    /// Check if a gateway URL is configured and create a client for it.
    fn gateway_client() -> Option<Self> {
        let gateway_url = std::env::var("CLAW_GATEWAY_URL").ok().filter(|v| !v.is_empty())?;
        let gateway_key = std::env::var("CLAW_GATEWAY_KEY").ok().filter(|v| !v.is_empty())?;
        let config = OpenAiCompatConfig {
            provider_name: "ClawGateway",
            api_key_env: "CLAW_GATEWAY_KEY",
            base_url_env: "CLAW_GATEWAY_URL",
            default_base_url: "",
        };
        let client = OpenAiCompatClient::new(gateway_key, config)
            .with_base_url(gateway_url.trim_end_matches('/').to_string() + "/v1");
        Some(Self::OpenRouter(client))
    }

    #[must_use]
    pub const fn provider_kind(&self) -> ProviderKind {
        match self {
            Self::ClawApi(_) => ProviderKind::ClawApi,
            Self::Xai(_) => ProviderKind::Xai,
            Self::OpenAi(_) => ProviderKind::OpenAi,
            Self::OpenRouter(_) => ProviderKind::OpenRouter,
        }
    }

    pub async fn send_message(
        &self,
        request: &MessageRequest,
    ) -> Result<MessageResponse, ApiError> {
        match self {
            Self::ClawApi(client) => send_via_provider(client, request).await,
            Self::Xai(client) | Self::OpenAi(client) | Self::OpenRouter(client) => {
                send_via_provider(client, request).await
            }
        }
    }

    pub async fn stream_message(
        &self,
        request: &MessageRequest,
    ) -> Result<MessageStream, ApiError> {
        match self {
            Self::ClawApi(client) => stream_via_provider(client, request)
                .await
                .map(MessageStream::ClawApi),
            Self::Xai(client) | Self::OpenAi(client) | Self::OpenRouter(client) => {
                stream_via_provider(client, request)
                    .await
                    .map(MessageStream::OpenAiCompat)
            }
        }
    }
}

#[derive(Debug)]
pub enum MessageStream {
    ClawApi(claw_provider::MessageStream),
    OpenAiCompat(openai_compat::MessageStream),
}

impl MessageStream {
    #[must_use]
    pub fn request_id(&self) -> Option<&str> {
        match self {
            Self::ClawApi(stream) => stream.request_id(),
            Self::OpenAiCompat(stream) => stream.request_id(),
        }
    }

    pub async fn next_event(&mut self) -> Result<Option<StreamEvent>, ApiError> {
        match self {
            Self::ClawApi(stream) => stream.next_event().await,
            Self::OpenAiCompat(stream) => stream.next_event().await,
        }
    }
}

pub use claw_provider::{
    oauth_token_is_expired, resolve_saved_oauth_token, resolve_startup_auth_source, OAuthTokenSet,
};
#[must_use]
pub fn read_base_url() -> String {
    claw_provider::read_base_url()
}

#[must_use]
pub fn read_xai_base_url() -> String {
    openai_compat::read_base_url(OpenAiCompatConfig::xai())
}

#[must_use]
pub fn read_openrouter_base_url() -> String {
    openai_compat::read_base_url(OpenAiCompatConfig::openrouter())
}

#[cfg(test)]
mod tests {
    use crate::providers::{detect_provider_kind, resolve_model_alias, ProviderKind};

    #[test]
    fn resolves_existing_and_grok_aliases() {
        assert_eq!(resolve_model_alias("opus"), "anthropic/claude-opus-4-6");
        assert_eq!(resolve_model_alias("sonnet"), "anthropic/claude-sonnet-4-6");
        assert_eq!(resolve_model_alias("grok"), "grok-3");
        assert_eq!(resolve_model_alias("grok-mini"), "grok-3-mini");
    }

    #[test]
    fn provider_detection_prefers_model_family() {
        assert_eq!(detect_provider_kind("grok-3"), ProviderKind::Xai);
        assert_eq!(
            detect_provider_kind("claude-sonnet-4-6"),
            ProviderKind::OpenRouter
        );
        assert_eq!(
            detect_provider_kind("opus"),
            ProviderKind::OpenRouter
        );
    }
}
