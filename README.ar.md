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

# إعادة كتابة مشروع Claw Code

<p align="center">
  <strong>⭐ أسرع مستودع في التاريخ يتجاوز 50 ألف نجمة، محققاً هذا الإنجاز في ساعتين فقط بعد النشر ⭐</strong>
</p>

<p align="center">
  <img src="assets/clawd-hero.jpeg" alt="Claw" width="300" />
</p>

<p align="center">
  <strong>أدوات Harness أفضل، وليس مجرد تخزين أرشيف Claw Code المُسرّب</strong>
</p>

> [!IMPORTANT]
> **نقل Rust قيد التنفيذ الآن** على فرع `dev/rust` ومن المتوقع دمجه في الفرع الرئيسي اليوم. يهدف تطبيق Rust إلى تقديم بيئة تشغيل harness أسرع وآمنة للذاكرة. ترقبوا — ستكون هذه النسخة النهائية للمشروع.

---

## نقل Rust

مساحة عمل Rust تحت `rust/` هي النقل الحالي بلغة الأنظمة للمشروع.

تشمل حالياً:

- `crates/api-client` — عميل API مع تجريد الموفر، OAuth، ودعم البث
- `crates/runtime` — حالة الجلسة، الضغط، تنظيم MCP، بناء الأوامر
- `crates/tools` — تعريفات بيان الأدوات وإطار التنفيذ
- `crates/commands` — أوامر السلاش، اكتشاف المهارات، وفحص التكوين
- `crates/plugins` — نموذج الإضافات، خط أنابيب الخطافات، والإضافات المجمعة
- `crates/compat-harness` — طبقة التوافق لتكامل المحرر العلوي
- `crates/claw-cli` — REPL تفاعلي، عرض Markdown، وتدفقات تهيئة المشروع

تشغيل بناء Rust:

```bash
cd rust
cargo build --release
```

## القصة الخلفية

في 31 مارس 2026 الساعة 4 صباحاً، استيقظت على هاتفي يفيض بالإشعارات. تم كشف الكود المصدري لـ Claw Code، وكان مجتمع المطورين بأكمله في حالة هيجان. كانت صديقتي في كوريا قلقة حقاً من أنني قد أواجه إجراءات قانونية من المؤلفين الأصليين لمجرد وجود الكود على جهازي — لذلك فعلت ما سيفعله أي مهندس تحت الضغط: جلست، نقلت الميزات الأساسية إلى Python من الصفر، ونشرتها قبل شروق الشمس.

تم تنظيم كل شيء من البداية إلى النهاية باستخدام [oh-my-codex (OmX)](https://github.com/Yeachan-Heo/oh-my-codex) بواسطة [@bellman_ych](https://x.com/bellman_ych). النتيجة هي إعادة كتابة Python في غرفة نظيفة تلتقط الأنماط المعمارية لـ harness وكيل Claw Code دون نسخ أي كود مصدري مملوك. **ترقبوا — نسخة أكثر قدرة في الطريق.**

![لقطة شاشة تغريدة](assets/tweet-screenshot.png)

## المبدعون في وول ستريت جورنال

لقد كنت مهتماً بشدة بـ **هندسة harness** — دراسة كيفية ربط أنظمة الوكلاء للأدوات، وتنظيم المهام، وإدارة سياق وقت التشغيل.

> — *وول ستريت جورنال*، 21 مارس 2026، [*"سباق التريليون دولار لأتمتة حياتنا بالكامل"*](https://lnkd.in/gs9td3qd)

![مقال WSJ](assets/wsj-feature.png)

---

## حالة النقل

شجرة الكود المصدري الرئيسية الآن Python أولاً.

- `src/` يحتوي على مساحة عمل نقل Python النشطة
- `tests/` يتحقق من مساحة عمل Python الحالية
- اللقطة المكشوفة لم تعد جزءاً من حالة المستودع المتتبعة

## لماذا توجد هذه الإعادة

درست في الأصل الكود المكشوف لفهم harness الخاص به وتوصيل الأدوات وسير عمل الوكيل. بعد قضاء المزيد من الوقت مع الأسئلة القانونية والأخلاقية، لم أرد أن تبقى اللقطة المكشوفة نفسها شجرة الكود المصدري الرئيسية المتتبعة.

## هيكل المستودع

```text
.
├── src/                                # مساحة عمل نقل Python
│   ├── __init__.py
│   ├── commands.py
│   ├── main.py
│   ├── models.py
│   ├── port_manifest.py
│   ├── query_engine.py
│   ├── task.py
│   └── tools.py
├── rust/                               # نقل Rust (claw CLI)
│   ├── crates/api/                     # عميل API + بث
│   ├── crates/runtime/                 # جلسة، أدوات، MCP، تكوين
│   ├── crates/claw-cli/               # ثنائي CLI تفاعلي
│   ├── crates/plugins/                 # نظام الإضافات
│   ├── crates/commands/                # أوامر السلاش
│   ├── crates/server/                  # خادم HTTP/SSE (axum)
│   ├── crates/lsp/                    # تكامل عميل LSP
│   └── crates/tools/                   # مواصفات الأدوات
├── tests/                              # تحقق Python
├── assets/omx/                         # لقطات شاشة سير عمل OmX
└── README.md
```

## البدء السريع

عرض ملخص نقل Python:

```bash
python3 -m src.main summary
```

طباعة بيان مساحة عمل Python الحالية:

```bash
python3 -m src.main manifest
```

تشغيل التحقق:

```bash
python3 -m unittest discover -s tests -v
```

## المجتمع

<p align="center">
  <a href="https://instruct.kr/"><img src="assets/instructkr.png" alt="instructkr" width="400" /></a>
</p>

انضم إلى [**Discord instructkr**](https://instruct.kr/) — أفضل مجتمع نماذج اللغة الكورية.

[![Discord](https://img.shields.io/badge/انضم%20إلى%20Discord-instruct.kr-5865F2?logo=discord&style=for-the-badge)](https://instruct.kr/)

## إخلاء مسؤولية الملكية / الانتماء

- هذا المستودع **لا** يدعي ملكية مواد Claw Code المصدرية الأصلية.
- هذا المستودع **غير تابع أو معتمد أو مُدار من قبل المؤلفين الأصليين**.
