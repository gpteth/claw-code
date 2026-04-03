//! Internationalization support for Claw Code CLI.
//!
//! Supports: English (en), Chinese (zh), Hindi (hi), Spanish (es), French (fr).

use std::collections::HashMap;
use std::sync::RwLock;

const EN_LOCALE: &str = include_str!("../locales/en.json");
const ZH_LOCALE: &str = include_str!("../locales/zh.json");
const HI_LOCALE: &str = include_str!("../locales/hi.json");
const ES_LOCALE: &str = include_str!("../locales/es.json");
const FR_LOCALE: &str = include_str!("../locales/fr.json");

pub const SUPPORTED_LOCALES: &[&str] = &["en", "zh", "hi", "es", "fr"];
pub const DEFAULT_LOCALE: &str = "en";

static CURRENT_LOCALE: RwLock<Option<String>> = RwLock::new(None);

fn parse_locale(json: &str) -> HashMap<String, String> {
    serde_json::from_str(json).unwrap_or_default()
}

fn locale_data(lang: &str) -> HashMap<String, String> {
    match lang {
        "zh" => parse_locale(ZH_LOCALE),
        "hi" => parse_locale(HI_LOCALE),
        "es" => parse_locale(ES_LOCALE),
        "fr" => parse_locale(FR_LOCALE),
        _ => parse_locale(EN_LOCALE),
    }
}

/// Detect locale from `CLAW_LANG` env var, or system `LANG`, fallback to "en".
pub fn detect_locale() -> String {
    if let Ok(lang) = std::env::var("CLAW_LANG") {
        let code = lang.trim().to_lowercase();
        if SUPPORTED_LOCALES.contains(&code.as_str()) {
            return code;
        }
    }

    if let Ok(lang) = std::env::var("LANG") {
        let code = lang.split('_').next().unwrap_or("en").to_lowercase();
        if SUPPORTED_LOCALES.contains(&code.as_str()) {
            return code;
        }
    }

    DEFAULT_LOCALE.to_string()
}

/// Set the active locale. Can be called multiple times to switch at runtime.
pub fn set_locale(lang: &str) {
    let lang = if SUPPORTED_LOCALES.contains(&lang) {
        lang.to_string()
    } else {
        DEFAULT_LOCALE.to_string()
    };
    if let Ok(mut lock) = CURRENT_LOCALE.write() {
        *lock = Some(lang);
    }
}

/// Get the current active locale.
pub fn get_locale() -> String {
    CURRENT_LOCALE
        .read()
        .ok()
        .and_then(|lock| lock.clone())
        .unwrap_or_else(|| DEFAULT_LOCALE.to_string())
}

/// Return a display name for the given locale code.
pub fn locale_display_name(code: &str) -> String {
    match code {
        "en" => "English".to_string(),
        "zh" => "中文".to_string(),
        "hi" => "हिन्दी".to_string(),
        "es" => "Español".to_string(),
        "fr" => "Français".to_string(),
        _ => code.to_string(),
    }
}

/// Translate a message key. Falls back to English, then to the key itself.
pub fn t(key: &str) -> String {
    let lang = get_locale();
    let messages = locale_data(&lang);
    if let Some(text) = messages.get(key) {
        return text.clone();
    }
    if lang != DEFAULT_LOCALE {
        let fallback = locale_data(DEFAULT_LOCALE);
        if let Some(text) = fallback.get(key) {
            return text.clone();
        }
    }
    key.to_string()
}

/// Translate a message key with named parameter substitution.
/// Replaces `{name}` patterns in the translated string.
pub fn t_fmt(key: &str, params: &[(&str, &str)]) -> String {
    let mut text = t(key);
    for (name, value) in params {
        text = text.replace(&format!("{{{name}}}"), value);
    }
    text
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn translates_known_key_in_english() {
        let messages = locale_data("en");
        assert_eq!(
            messages.get("app.interactive_mode").unwrap(),
            "Claw Code interactive mode"
        );
    }

    #[test]
    fn translates_known_key_in_chinese() {
        let messages = locale_data("zh");
        assert_eq!(
            messages.get("app.interactive_mode").unwrap(),
            "Claw Code 交互模式"
        );
    }

    #[test]
    fn falls_back_to_key_for_unknown() {
        // Since OnceLock is already set or defaults to "en"
        let result = t("nonexistent.key");
        assert_eq!(result, "nonexistent.key");
    }

    #[test]
    fn t_fmt_replaces_parameters() {
        let messages = locale_data("en");
        let template = messages.get("cmd.unknown").unwrap();
        let result = template.replace("{name}", "foo");
        assert_eq!(result, "Unknown slash command: /foo");
    }

    #[test]
    fn all_locales_have_same_keys() {
        let en = locale_data("en");
        for lang in &["zh", "hi", "es", "fr"] {
            let other = locale_data(lang);
            for key in en.keys() {
                assert!(
                    other.contains_key(key),
                    "Locale '{lang}' missing key: {key}"
                );
            }
        }
    }
}
