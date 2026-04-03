<p align="center">
  <a href="README.md">English</a> |
  <a href="README.zh.md">中文</a> |
  <a href="README.hi.md">हिन्दी</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.fr.md">Français</a> |
  <a href="README.ar.md">العربية</a> |
  <a href="README.bn.md">বাংলা</a> |
  <a href="README.pt.md">Português</a> |
  <a href="README.ru.md">Русский</a> |
  <a href="README.ja.md">日本語</a>
</p>

# Reescritura del Proyecto Claw Code

<p align="center">
  <strong>⭐ El repositorio más rápido de la historia en superar las 50K estrellas, alcanzando el hito en solo 2 horas después de su publicación ⭐</strong>
</p>

<p align="center">
  <img src="assets/clawd-hero.jpeg" alt="Claw" width="300" />
</p>

<p align="center">
  <strong>Mejores herramientas Harness, no simplemente almacenar el archivo del Claw Code filtrado</strong>
</p>

> [!IMPORTANT]
> **El port a Rust está en progreso** en la rama `dev/rust` y se espera que se fusione en main hoy. La implementación en Rust busca ofrecer un runtime de harness más rápido y seguro en memoria. Manténgase atento — esta será la versión definitiva del proyecto.

---

## Port a Rust

El espacio de trabajo Rust bajo `rust/` es el port actual en lenguaje de sistemas del proyecto.

Actualmente incluye:

- `crates/api-client` — Cliente API con abstracción de proveedores, OAuth y soporte de streaming
- `crates/runtime` — Estado de sesión, compactación, orquestación MCP, construcción de prompts
- `crates/tools` — Definiciones de manifiesto de herramientas y marco de ejecución
- `crates/commands` — Comandos slash, descubrimiento de habilidades e inspección de configuración
- `crates/plugins` — Modelo de plugins, pipeline de hooks y plugins incluidos
- `crates/compat-harness` — Capa de compatibilidad para integración con editor upstream
- `crates/claw-cli` — REPL interactivo, renderizado Markdown y flujos de bootstrap/init del proyecto

Ejecutar la compilación Rust:

```bash
cd rust
cargo build --release
```

## Historia

El 31 de marzo de 2026 a las 4 AM, me desperté con mi teléfono explotando de notificaciones. El código fuente de Claw Code había sido expuesto y toda la comunidad de desarrolladores estaba frenética. Mi novia en Corea estaba genuinamente preocupada de que pudiera enfrentar acciones legales de los autores originales solo por tener el código en mi máquina — así que hice lo que cualquier ingeniero haría bajo presión: me senté, porté las características principales a Python desde cero y lo publiqué antes de que saliera el sol.

Todo fue orquestado de extremo a extremo usando [oh-my-codex (OmX)](https://github.com/Yeachan-Heo/oh-my-codex) por [@bellman_ych](https://x.com/bellman_ych). El resultado es una reescritura limpia en Python que captura los patrones arquitectónicos del harness de agente de Claw Code sin copiar ningún código fuente propietario. **Manténgase atento — una versión mucho más capaz está en camino.**

![Captura de tweet](assets/tweet-screenshot.png)

## Los creadores destacados en The Wall Street Journal

He estado profundamente interesado en la **ingeniería de harness** — estudiar cómo los sistemas de agentes conectan herramientas, orquestan tareas y gestionan el contexto de ejecución.

> — *The Wall Street Journal*, 21 de marzo de 2026, [*"La carrera del billón de dólares para automatizar nuestras vidas enteras"*](https://lnkd.in/gs9td3qd)

![Artículo WSJ](assets/wsj-feature.png)

---

## Estado del Port

El árbol de código fuente principal es ahora Python-first.

- `src/` contiene el espacio de trabajo activo de portabilidad Python
- `tests/` verifica el espacio de trabajo Python actual
- La snapshot expuesta ya no es parte del estado del repositorio rastreado

## Por qué existe esta reescritura

Originalmente estudié el código expuesto para entender su harness, conexión de herramientas y flujo de trabajo de agentes. Después de dedicar más tiempo a las cuestiones legales y éticas, no quise que la snapshot expuesta siguiera siendo el árbol de código fuente principal rastreado.

## Diseño del Repositorio

```text
.
├── src/                                # Espacio de trabajo de portabilidad Python
│   ├── __init__.py
│   ├── commands.py
│   ├── main.py
│   ├── models.py
│   ├── port_manifest.py
│   ├── query_engine.py
│   ├── task.py
│   └── tools.py
├── rust/                               # Port Rust (claw CLI)
│   ├── crates/api/                     # Cliente API + streaming
│   ├── crates/runtime/                 # Sesión, herramientas, MCP, config
│   ├── crates/claw-cli/               # Binario CLI interactivo
│   ├── crates/plugins/                 # Sistema de plugins
│   ├── crates/commands/                # Comandos slash
│   ├── crates/server/                  # Servidor HTTP/SSE (axum)
│   ├── crates/lsp/                    # Integración cliente LSP
│   └── crates/tools/                   # Especificaciones de herramientas
├── tests/                              # Verificación Python
├── assets/omx/                         # Capturas del flujo de trabajo OmX
└── README.md
```

## Inicio Rápido

Renderizar el resumen de portabilidad Python:

```bash
python3 -m src.main summary
```

Imprimir el manifiesto actual del espacio de trabajo Python:

```bash
python3 -m src.main manifest
```

Ejecutar verificación:

```bash
python3 -m unittest discover -s tests -v
```

## Comunidad

<p align="center">
  <a href="https://instruct.kr/"><img src="assets/instructkr.png" alt="instructkr" width="400" /></a>
</p>

Únase al [**Discord de instructkr**](https://instruct.kr/) — la mejor comunidad de modelos de lenguaje en coreano.

[![Discord](https://img.shields.io/badge/Unirse%20a%20Discord-instruct.kr-5865F2?logo=discord&style=for-the-badge)](https://instruct.kr/)

## Descargo de responsabilidad de propiedad/afiliación

- Este repositorio **no** reclama la propiedad del material fuente original de Claw Code.
- Este repositorio **no está afiliado, respaldado ni mantenido por los autores originales**.
