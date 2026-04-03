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

# 重写 Claw Code 项目

<p align="center">
  <strong>⭐ 历史上增长最快的仓库，发布仅 2 小时便突破 50K 星标 ⭐</strong>
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
  <strong>更好的 Harness 工具，而非仅存储泄露的 Claw Code 存档</strong>
</p>

<p align="center">
  <a href="https://github.com/sponsors/instructkr"><img src="https://img.shields.io/badge/赞助-%E2%9D%A4-pink?logo=github&style=for-the-badge" alt="在 GitHub 上赞助" /></a>
</p>

> [!IMPORTANT]
> **Rust 移植正在进行中**，位于 [`dev/rust`](https://github.com/instructkr/claw-code/tree/dev/rust) 分支，预计今日合并到主分支。Rust 实现旨在提供更快、内存安全的 harness 运行时。敬请期待——这将成为项目的最终版本。

> 如果您觉得这项工作有用，请考虑[在 GitHub 上赞助 @instructkr](https://github.com/sponsors/instructkr)，以支持持续的开源 harness 工程研究。

---

## Rust 移植

`rust/` 目录下的 Rust 工作区是本项目的当前系统语言移植版本。

目前包含：

- `crates/api-client` — API 客户端，支持提供商抽象、OAuth 和流式传输
- `crates/runtime` — 会话状态、压缩、MCP 编排、提示构建
- `crates/tools` — 工具清单定义和执行框架
- `crates/commands` — 斜杠命令、技能发现和配置检查
- `crates/plugins` — 插件模型、钩子管道和内置插件
- `crates/compat-harness` — 上游编辑器集成的兼容层
- `crates/claw-cli` — 交互式 REPL、Markdown 渲染和项目引导/初始化流程

运行 Rust 构建：

```bash
cd rust
cargo build --release
```

## 背景故事

2026 年 3 月 31 日凌晨 4 点，我被手机上疯狂涌入的通知惊醒。Claw Code 源码已被泄露，整个开发者社区都在沸腾。我在韩国的女友真的很担心我可能会因为电脑上有这些代码而面临原作者的法律诉讼——所以我做了任何工程师在压力下都会做的事：坐下来，从零开始将核心功能移植到 Python，并在太阳升起之前推送了代码。

整个过程使用 [oh-my-codex (OmX)](https://github.com/Yeachan-Heo/oh-my-codex)（由 [@bellman_ych](https://x.com/bellman_ych) 开发）进行端到端编排——这是一个建立在 OpenAI Codex ([@OpenAIDevs](https://x.com/OpenAIDevs)) 之上的工作流层。我使用 `$team` 模式进行并行代码审查，使用 `$ralph` 模式进行持久执行循环和架构级验证。从阅读原始 harness 结构到生成带有测试的可运行 Python 代码树的整个移植会话，都由 OmX 编排驱动。

结果是一个干净室（clean-room）Python 重写版本，它捕获了 Claw Code agent harness 的架构模式，而没有复制任何专有源代码。我现在正在积极与 [@bellman_ych](https://x.com/bellman_ych)——OmX 的创建者本人——合作推进此项目。基础 Python 框架已经建立并可以运行，但我们才刚刚开始。**敬请期待——一个更强大的版本即将到来。**

Rust 移植使用 [oh-my-codex (OmX)](https://github.com/Yeachan-Heo/oh-my-codex) 和 [oh-my-opencode (OmO)](https://github.com/code-yeongyu/oh-my-openagent) 开发：OmX 驱动了脚手架、编排和架构方向，而 OmO 用于后期实现加速和验证支持。

https://github.com/instructkr/claw-code

![推文截图](assets/tweet-screenshot.png)

## 创建者被华尔街日报报道 — 致 Claw Code 的狂热粉丝们

我对 **harness 工程** 有着深厚的兴趣——研究 agent 系统如何连接工具、编排任务和管理运行时上下文。这不是突然的事情。华尔街日报本月早些时候报道了我的工作，记录了我如何成为探索这些系统的最活跃的超级用户之一：

> AI 初创公司员工 Sigrid Jin，参加了首尔晚宴，去年单独使用了 250 亿个 Claw Code 代币。当时，使用限制更宽松，让早期爱好者能够以极低的成本达到数百亿代币。
>
> 尽管与 Claw Code 相处了无数个小时，Jin 并不忠于任何一个 AI 实验室。他说，现有的工具各有优缺点。Codex 的推理能力更强，而 Claw Code 生成的代码更干净、更易分享。
>
> Jin 今年二月飞往旧金山参加 Claw Code 的一周年派对，参加者排队与 Cherny 交流。人群中有一位比利时的执业心脏病专家，他开发了一个帮助患者导航医疗的应用程序，还有一位加利福尼亚律师，他使用 Claw Code 制作了一个自动化建筑许可审批的工具。
>
> "这基本上就像一个分享派对，"Jin 说。"有律师，有医生，有牙医。他们没有软件工程背景。"
>
> — *华尔街日报*，2026 年 3 月 21 日，[*"万亿美元的自动化我们整个生活的竞赛"*](https://lnkd.in/gs9td3qd)

![华尔街日报报道](assets/wsj-feature.png)

---

## 移植状态

主源代码树现在以 Python 为主。

- `src/` 包含活跃的 Python 移植工作区
- `tests/` 验证当前的 Python 工作区
- 泄露的快照不再是跟踪仓库状态的一部分

当前的 Python 工作区尚不是原始系统的完全一对一替代品，但主要实现界面现在是 Python。

## 为什么存在这个重写版本

我最初研究泄露的代码库是为了了解其 harness、工具连接和 agent 工作流。在花更多时间思考法律和伦理问题后——并在阅读了下面链接的文章之后——我不希望泄露的快照本身继续作为主要跟踪源代码树。

本仓库现在专注于 Python 移植工作。

## 仓库布局

```text
.
├── src/                                # Python 移植工作区
│   ├── __init__.py
│   ├── commands.py
│   ├── main.py
│   ├── models.py
│   ├── port_manifest.py
│   ├── query_engine.py
│   ├── task.py
│   └── tools.py
├── rust/                               # Rust 移植（claw CLI）
│   ├── crates/api/                     # API 客户端 + 流式传输
│   ├── crates/runtime/                 # 会话、工具、MCP、配置
│   ├── crates/claw-cli/               # 交互式 CLI 二进制文件
│   ├── crates/plugins/                 # 插件系统
│   ├── crates/commands/                # 斜杠命令
│   ├── crates/server/                  # HTTP/SSE 服务器 (axum)
│   ├── crates/lsp/                    # LSP 客户端集成
│   └── crates/tools/                   # 工具规范
├── tests/                              # Python 验证
├── assets/omx/                         # OmX 工作流截图
├── 2026-03-09-is-legal-the-same-as-legitimate-ai-reimplementation-and-the-erosion-of-copyleft.md
└── README.md
```

## Python 工作区概览

新的 Python `src/` 目录树目前提供：

- **`port_manifest.py`** — 总结当前 Python 工作区结构
- **`models.py`** — 子系统、模块和待办事项状态的数据类
- **`commands.py`** — Python 端命令移植元数据
- **`tools.py`** — Python 端工具移植元数据
- **`query_engine.py`** — 从活跃工作区渲染 Python 移植摘要
- **`main.py`** — 清单和摘要输出的 CLI 入口点

## 快速开始

渲染 Python 移植摘要：

```bash
python3 -m src.main summary
```

打印当前 Python 工作区清单：

```bash
python3 -m src.main manifest
```

列出当前 Python 模块：

```bash
python3 -m src.main subsystems --limit 16
```

运行验证：

```bash
python3 -m unittest discover -s tests -v
```

对比本地忽略的存档运行奇偶校验审计（如果存在）：

```bash
python3 -m src.main parity-audit
```

检查镜像的命令/工具清单：

```bash
python3 -m src.main commands --limit 10
python3 -m src.main tools --limit 10
```

## 当前奇偶校验检查点

移植现在更紧密地镜像了存档的根入口文件界面、顶级子系统名称和命令/工具清单。然而，它**尚未**成为原始 TypeScript 系统的完全运行时等效替代品；Python 代码树仍然包含比存档源更少的可执行运行时切片。

## 使用 `oh-my-codex` 和 `oh-my-opencode` 构建

本仓库的移植、干净室加固和验证工作流由 Yeachan Heo 的工具栈进行 AI 辅助，以 **oh-my-codex (OmX)** 作为主要的脚手架和编排层。

- [**oh-my-codex (OmX)**](https://github.com/Yeachan-Heo/oh-my-codex) — 脚手架、编排、架构方向和核心移植工作流
- [**oh-my-opencode (OmO)**](https://github.com/code-yeongyu/oh-my-openagent) — 实现加速、清理和验证支持

移植期间使用的关键工作流模式：

- **`$team` 模式：** 协调的并行审查和架构反馈
- **`$ralph` 模式：** 持久执行、验证和完成纪律
- **干净室通道：** 命名/品牌清理、QA 和 Rust 工作区的发布验证
- **手动和实时验证：** 在发布前进行构建、测试、手动 QA 和真实 API 路径验证

### OmX 工作流截图

![OmX 工作流截图 1](assets/omx/omx-readme-review-1.png)

*Ralph/team 编排视图，README 和文章上下文正在终端面板中审查。*

![OmX 工作流截图 2](assets/omx/omx-readme-review-2.png)

*最终 README 措辞通过期间的分屏审查和验证流程。*

## 社区

<p align="center">
  <a href="https://instruct.kr/"><img src="assets/instructkr.png" alt="instructkr" width="400" /></a>
</p>

加入 [**instructkr Discord**](https://instruct.kr/) — 最好的韩语语言模型社区。来讨论 LLM、harness 工程、agent 工作流以及更多内容。

[![Discord](https://img.shields.io/badge/加入%20Discord-instruct.kr-5865F2?logo=discord&style=for-the-badge)](https://instruct.kr/)

## Star 历史

请参见本 README 顶部的图表。

## 所有权/关联声明

- 本仓库**不**声称拥有原始 Claw Code 源材料的所有权。
- 本仓库与原始作者**没有关联、未经其认可，也不由其维护**。
