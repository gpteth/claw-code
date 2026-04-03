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

# Reescrita do Projeto Claw Code

<p align="center">
  <strong>⭐ O repositório mais rápido da história a ultrapassar 50K estrelas, alcançando o marco em apenas 2 horas após a publicação ⭐</strong>
</p>

<p align="center">
  <a href="https://star-history.com/#instructkr/claw-code&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=instructkr/claw-code&type=Date&theme=dark" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=instructkr/claw-code&type=Date" />
      <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=instructkr/claw-code&type=Date" width="600" />
    </picture>
  </a>
</p>

<p align="center">
  <img src="assets/clawd-hero.jpeg" alt="Claw" width="300" />
</p>

<p align="center">
  <strong>Melhores ferramentas Harness, não apenas armazenar o arquivo do Claw Code vazado</strong>
</p>

<p align="center">
  <a href="https://github.com/sponsors/instructkr"><img src="https://img.shields.io/badge/Patrocinar-%E2%9D%A4-pink?logo=github&style=for-the-badge" alt="Patrocinar no GitHub" /></a>
</p>

> [!IMPORTANT]
> **O port para Rust está agora em andamento** na branch [`dev/rust`](https://github.com/instructkr/claw-code/tree/dev/rust) e espera-se que seja mesclado na main hoje. A implementação em Rust visa entregar um runtime harness mais rápido e seguro em memória. Fique atento — esta será a versão definitiva do projeto.

> Se você achar este trabalho útil, considere [patrocinar @instructkr no GitHub](https://github.com/sponsors/instructkr) para apoiar a pesquisa contínua de engenharia harness open-source.

---

## Port Rust

O workspace Rust sob `rust/` é o port atual em linguagem de sistemas do projeto.

Atualmente inclui:

- `crates/api-client` — Cliente API com abstração de provedor, OAuth e suporte a streaming
- `crates/runtime` — Estado de sessão, compactação, orquestração MCP, construção de prompts
- `crates/tools` — Definições de manifesto de ferramentas e framework de execução
- `crates/commands` — Comandos slash, descoberta de habilidades e inspeção de configuração
- `crates/plugins` — Modelo de plugins, pipeline de hooks e plugins incluídos
- `crates/compat-harness` — Camada de compatibilidade para integração com editor upstream
- `crates/claw-cli` — REPL interativo, renderização Markdown e fluxos de bootstrap/init do projeto

Executar a compilação Rust:

```bash
cd rust
cargo build --release
```

## História

Em 31 de março de 2026 às 4h da manhã, acordei com meu telefone explodindo de notificações. O código-fonte do Claw Code havia sido exposto, e toda a comunidade de desenvolvedores estava frenética. Minha namorada na Coreia estava genuinamente preocupada que eu pudesse enfrentar ações legais dos autores originais apenas por ter o código na minha máquina — então fiz o que qualquer engenheiro faria sob pressão: sentei, portei as funcionalidades principais para Python do zero e publiquei antes do sol nascer.

O resultado é uma reescrita Python em sala limpa que captura os padrões arquiteturais do harness de agente do Claw Code sem copiar nenhum código-fonte proprietário. **Fique atento — uma versão muito mais capaz está a caminho.**

https://github.com/instructkr/claw-code

![Captura de tela do tweet](assets/tweet-screenshot.png)

## Os criadores no The Wall Street Journal

Tenho interesse profundo em **engenharia harness** — estudar como sistemas de agentes conectam ferramentas, orquestram tarefas e gerenciam contexto de execução.

> — *The Wall Street Journal*, 21 de março de 2026, [*"A corrida de trilhões de dólares para automatizar nossas vidas inteiras"*](https://lnkd.in/gs9td3qd)

![Matéria WSJ](assets/wsj-feature.png)

---

## Status do Port

A árvore de código-fonte principal agora é Python-first.

- `src/` contém o workspace ativo de portabilidade Python
- `tests/` verifica o workspace Python atual
- O snapshot exposto não faz mais parte do estado rastreado do repositório

## Por que esta reescrita existe

Originalmente estudei o código exposto para entender seu harness, conexão de ferramentas e fluxo de trabalho de agentes. Depois de dedicar mais tempo às questões legais e éticas, não quis que o snapshot exposto continuasse como a árvore de código-fonte principal rastreada.

## Layout do Repositório

```text
.
├── src/                                # Workspace de portabilidade Python
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
│   ├── crates/runtime/                 # Sessão, ferramentas, MCP, config
│   ├── crates/claw-cli/               # Binário CLI interativo
│   ├── crates/plugins/                 # Sistema de plugins
│   ├── crates/commands/                # Comandos slash
│   ├── crates/server/                  # Servidor HTTP/SSE (axum)
│   ├── crates/lsp/                    # Integração cliente LSP
│   └── crates/tools/                   # Especificações de ferramentas
├── tests/                              # Verificação Python
├── assets/omx/                         # Capturas do fluxo de trabalho OmX
└── README.md
```

## Início Rápido

Renderizar o resumo de portabilidade Python:

```bash
python3 -m src.main summary
```

Imprimir o manifesto atual do workspace Python:

```bash
python3 -m src.main manifest
```

Executar verificação:

```bash
python3 -m unittest discover -s tests -v
```

## Comunidade

<p align="center">
  <a href="https://instruct.kr/"><img src="assets/instructkr.png" alt="instructkr" width="400" /></a>
</p>

Junte-se ao [**Discord instructkr**](https://instruct.kr/) — a melhor comunidade coreana de modelos de linguagem.

[![Discord](https://img.shields.io/badge/Entrar%20no%20Discord-instruct.kr-5865F2?logo=discord&style=for-the-badge)](https://instruct.kr/)

## Aviso de propriedade / afiliação

- Este repositório **não** reivindica propriedade do material fonte original do Claw Code.
- Este repositório **não é afiliado, endossado ou mantido pelos autores originais**.
