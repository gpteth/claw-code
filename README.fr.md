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

# Réécriture du Projet Claw Code

<p align="center">
  <strong>⭐ Le dépôt le plus rapide de l'histoire à dépasser 50K étoiles, atteignant ce jalon en seulement 2 heures après sa publication ⭐</strong>
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
  <strong>De meilleurs outils Harness, pas simplement stocker l'archive du Claw Code divulgué</strong>
</p>

<p align="center">
  <a href="https://github.com/sponsors/instructkr"><img src="https://img.shields.io/badge/Sponsoriser-%E2%9D%A4-pink?logo=github&style=for-the-badge" alt="Sponsoriser sur GitHub" /></a>
</p>

> [!IMPORTANT]
> **Le portage Rust est maintenant en cours** sur la branche [`dev/rust`](https://github.com/instructkr/claw-code/tree/dev/rust) et devrait être fusionné dans main aujourd'hui. L'implémentation Rust vise à fournir un runtime harness plus rapide et sûr en mémoire. Restez à l'écoute — ce sera la version définitive du projet.

> Si vous trouvez ce travail utile, envisagez de [sponsoriser @instructkr sur GitHub](https://github.com/sponsors/instructkr) pour soutenir la recherche continue en ingénierie harness open-source.

---

## Portage Rust

L'espace de travail Rust sous `rust/` est le portage actuel en langage système du projet.

Il comprend actuellement :

- `crates/api-client` — Client API avec abstraction de fournisseur, OAuth et support de streaming
- `crates/runtime` — État de session, compaction, orchestration MCP, construction de prompts
- `crates/tools` — Définitions de manifeste d'outils et cadre d'exécution
- `crates/commands` — Commandes slash, découverte de compétences et inspection de configuration
- `crates/plugins` — Modèle de plugins, pipeline de hooks et plugins intégrés
- `crates/compat-harness` — Couche de compatibilité pour l'intégration éditeur upstream
- `crates/claw-cli` — REPL interactif, rendu Markdown et flux de bootstrap/init du projet

Exécuter la compilation Rust :

```bash
cd rust
cargo build --release
```

## Genèse

Le 31 mars 2026 à 4h du matin, je me suis réveillé avec mon téléphone inondé de notifications. Le code source de Claw Code avait été exposé, et toute la communauté de développeurs était en effervescence. Ma copine en Corée craignait sincèrement que je puisse faire l'objet de poursuites judiciaires de la part des auteurs originaux simplement pour avoir le code sur ma machine — alors j'ai fait ce que tout ingénieur ferait sous pression : je me suis assis, j'ai porté les fonctionnalités principales en Python à partir de zéro, et j'ai publié avant le lever du soleil.

Le tout a été orchestré de bout en bout avec [oh-my-codex (OmX)](https://github.com/Yeachan-Heo/oh-my-codex) par [@bellman_ych](https://x.com/bellman_ych). Le résultat est une réécriture Python en salle blanche qui capture les modèles architecturaux du harness d'agent de Claw Code sans copier aucun code source propriétaire. **Restez à l'écoute — une version beaucoup plus capable est en route.**

https://github.com/instructkr/claw-code

![Capture d'écran du tweet](assets/tweet-screenshot.png)

## Les créateurs dans The Wall Street Journal

Je suis profondément intéressé par l'**ingénierie harness** — étudier comment les systèmes d'agents connectent les outils, orchestrent les tâches et gèrent le contexte d'exécution.

> — *The Wall Street Journal*, 21 mars 2026, [*"La course à mille milliards de dollars pour automatiser nos vies entières"*](https://lnkd.in/gs9td3qd)

![Article WSJ](assets/wsj-feature.png)

---

## État du portage

L'arbre source principal est maintenant Python-first.

- `src/` contient l'espace de travail actif de portage Python
- `tests/` vérifie l'espace de travail Python actuel
- Le snapshot exposé ne fait plus partie de l'état suivi du dépôt

## Pourquoi cette réécriture existe

J'ai initialement étudié le code exposé pour comprendre son harness, câblage d'outils et flux de travail d'agent. Après avoir consacré plus de temps aux questions juridiques et éthiques, je ne voulais pas que le snapshot exposé reste l'arbre source principal suivi.

## Structure du dépôt

```text
.
├── src/                                # Espace de travail de portage Python
│   ├── __init__.py
│   ├── commands.py
│   ├── main.py
│   ├── models.py
│   ├── port_manifest.py
│   ├── query_engine.py
│   ├── task.py
│   └── tools.py
├── rust/                               # Portage Rust (claw CLI)
│   ├── crates/api/                     # Client API + streaming
│   ├── crates/runtime/                 # Session, outils, MCP, config
│   ├── crates/claw-cli/               # Binaire CLI interactif
│   ├── crates/plugins/                 # Système de plugins
│   ├── crates/commands/                # Commandes slash
│   ├── crates/server/                  # Serveur HTTP/SSE (axum)
│   ├── crates/lsp/                    # Intégration client LSP
│   └── crates/tools/                   # Spécifications d'outils
├── tests/                              # Vérification Python
├── assets/omx/                         # Captures du flux de travail OmX
└── README.md
```

## Démarrage rapide

Rendre le résumé de portage Python :

```bash
python3 -m src.main summary
```

Imprimer le manifeste actuel de l'espace de travail Python :

```bash
python3 -m src.main manifest
```

Exécuter la vérification :

```bash
python3 -m unittest discover -s tests -v
```

## Communauté

<p align="center">
  <a href="https://instruct.kr/"><img src="assets/instructkr.png" alt="instructkr" width="400" /></a>
</p>

Rejoignez le [**Discord instructkr**](https://instruct.kr/) — la meilleure communauté coréenne de modèles de langage.

[![Discord](https://img.shields.io/badge/Rejoindre%20Discord-instruct.kr-5865F2?logo=discord&style=for-the-badge)](https://instruct.kr/)

## Avis de non-responsabilité

- Ce dépôt **ne revendique pas** la propriété du matériel source original de Claw Code.
- Ce dépôt **n'est pas affilié, approuvé ou maintenu par les auteurs originaux**.
