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

# Claw Code プロジェクトの書き直し

<p align="center">
  <strong>⭐ 史上最速で50Kスターを突破したリポジトリ、公開からわずか2時間でマイルストーン達成 ⭐</strong>
</p>

<p align="center">
  <img src="assets/clawd-hero.jpeg" alt="Claw" width="300" />
</p>

<p align="center">
  <strong>リークされた Claw Code のアーカイブを保存するだけでなく、より優れた Harness ツールを</strong>
</p>

> [!IMPORTANT]
> **Rust ポートが現在進行中**です。`dev/rust` ブランチで開発中で、本日 main にマージ予定です。Rust 実装は、より高速でメモリセーフな harness ランタイムの提供を目指しています。ご期待ください — これがプロジェクトの決定版となります。

---

## Rust ポート

`rust/` 配下の Rust ワークスペースは、プロジェクトの現在のシステム言語ポートです。

現在含まれるもの:

- `crates/api-client` — プロバイダー抽象化、OAuth、ストリーミングサポート付き API クライアント
- `crates/runtime` — セッション状態、コンパクション、MCP オーケストレーション、プロンプト構築
- `crates/tools` — ツールマニフェスト定義と実行フレームワーク
- `crates/commands` — スラッシュコマンド、スキル検出、設定検査
- `crates/plugins` — プラグインモデル、フックパイプライン、バンドルプラグイン
- `crates/compat-harness` — アップストリームエディター統合のための互換性レイヤー
- `crates/claw-cli` — インタラクティブ REPL、Markdown レンダリング、プロジェクトブートストラップ/初期化フロー

Rust ビルドの実行:

```bash
cd rust
cargo build --release
```

## 背景

2026年3月31日午前4時、大量の通知で目が覚めました。Claw Code のソースコードが流出し、開発者コミュニティ全体が騒然としていました。韓国にいる彼女は、マシンにコードがあるだけで原著作者から法的措置を受けるかもしれないと本気で心配していました — なので、プレッシャーの中でエンジニアなら誰でもすることをしました：座って、コア機能をゼロから Python にポートし、日の出前にプッシュしました。

すべて [oh-my-codex (OmX)](https://github.com/Yeachan-Heo/oh-my-codex)（[@bellman_ych](https://x.com/bellman_ych) 開発）によってエンドツーエンドでオーケストレーションされました。結果は、プロプライエタリなソースコードをコピーすることなく、Claw Code のエージェント harness のアーキテクチャパターンを捉えたクリーンルーム Python 書き直しです。**ご期待ください — はるかに強力なバージョンが間もなく登場します。**

![ツイートスクリーンショット](assets/tweet-screenshot.png)

## クリエイターがウォール・ストリート・ジャーナルに掲載

私は **harness エンジニアリング** に深い関心を持っています — エージェントシステムがどのようにツールを接続し、タスクをオーケストレーションし、ランタイムコンテキストを管理するかを研究しています。

> — *ウォール・ストリート・ジャーナル*、2026年3月21日、[*「私たちの生活全体を自動化する1兆ドルの競争」*](https://lnkd.in/gs9td3qd)

![WSJ 記事](assets/wsj-feature.png)

---

## ポーティング状況

メインソースツリーは現在 Python ファーストです。

- `src/` にアクティブな Python ポーティングワークスペースがあります
- `tests/` が現在の Python ワークスペースを検証します
- 流出したスナップショットはもはやトラッキングされるリポジトリ状態の一部ではありません

## この書き直しが存在する理由

元々、流出したコードベースを研究して、その harness、ツール配線、エージェントワークフローを理解しました。法的・倫理的な問題により多くの時間を費やした後、流出したスナップショット自体をメインのトラッキング対象ソースツリーとして残したくありませんでした。

## リポジトリレイアウト

```text
.
├── src/                                # Python ポーティングワークスペース
│   ├── __init__.py
│   ├── commands.py
│   ├── main.py
│   ├── models.py
│   ├── port_manifest.py
│   ├── query_engine.py
│   ├── task.py
│   └── tools.py
├── rust/                               # Rust ポート (claw CLI)
│   ├── crates/api/                     # API クライアント + ストリーミング
│   ├── crates/runtime/                 # セッション、ツール、MCP、設定
│   ├── crates/claw-cli/               # インタラクティブ CLI バイナリ
│   ├── crates/plugins/                 # プラグインシステム
│   ├── crates/commands/                # スラッシュコマンド
│   ├── crates/server/                  # HTTP/SSE サーバー (axum)
│   ├── crates/lsp/                    # LSP クライアント統合
│   └── crates/tools/                   # ツール仕様
├── tests/                              # Python 検証
├── assets/omx/                         # OmX ワークフロースクリーンショット
└── README.md
```

## クイックスタート

Python ポーティングサマリーをレンダリング:

```bash
python3 -m src.main summary
```

現在の Python ワークスペースマニフェストを表示:

```bash
python3 -m src.main manifest
```

検証を実行:

```bash
python3 -m unittest discover -s tests -v
```

## コミュニティ

<p align="center">
  <a href="https://instruct.kr/"><img src="assets/instructkr.png" alt="instructkr" width="400" /></a>
</p>

[**instructkr Discord**](https://instruct.kr/) に参加しましょう — 最高の韓国語言語モデルコミュニティです。

[![Discord](https://img.shields.io/badge/Discord%20に参加-instruct.kr-5865F2?logo=discord&style=for-the-badge)](https://instruct.kr/)

## 所有権 / 提携に関する免責事項

- このリポジトリは、オリジナルの Claw Code ソースマテリアルの所有権を**主張しません**。
- このリポジトリは、オリジナルの著者と**提携、承認、または保守されているものではありません**。
