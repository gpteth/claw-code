"""Internationalization support for Claw Code.

Supports: English (en), Chinese (zh), Hindi (hi), Spanish (es), French (fr).
"""
from __future__ import annotations

import json
import locale
import os
from functools import lru_cache
from pathlib import Path

LOCALES_DIR = Path(__file__).resolve().parent / 'locales'
SUPPORTED_LOCALES = ('en', 'zh', 'hi', 'es', 'fr')
DEFAULT_LOCALE = 'en'

_current_locale: str = DEFAULT_LOCALE


@lru_cache(maxsize=8)
def _load_locale(lang: str) -> dict[str, str]:
    path = LOCALES_DIR / f'{lang}.json'
    if not path.exists():
        if lang != DEFAULT_LOCALE:
            return _load_locale(DEFAULT_LOCALE)
        return {}
    return json.loads(path.read_text(encoding='utf-8'))


def detect_locale() -> str:
    """Detect locale from CLAW_LANG env var, or system locale, fallback to 'en'."""
    env_lang = os.environ.get('CLAW_LANG', '').strip()
    if env_lang and env_lang in SUPPORTED_LOCALES:
        return env_lang

    sys_locale = locale.getdefaultlocale()[0] or ''
    lang_code = sys_locale.split('_')[0].lower()
    if lang_code in SUPPORTED_LOCALES:
        return lang_code

    return DEFAULT_LOCALE


def set_locale(lang: str) -> None:
    """Set the active locale."""
    global _current_locale
    if lang in SUPPORTED_LOCALES:
        _current_locale = lang
    else:
        _current_locale = DEFAULT_LOCALE


def get_locale() -> str:
    """Return the current active locale."""
    return _current_locale


LOCALE_DISPLAY_NAMES = {
    'en': 'English',
    'zh': '中文',
    'hi': 'हिन्दी',
    'es': 'Español',
    'fr': 'Français',
}


def locale_display_name(code: str) -> str:
    """Return a human-readable display name for a locale code."""
    return LOCALE_DISPLAY_NAMES.get(code, code)


def t(key: str, **kwargs: object) -> str:
    """Translate a message key, with optional format parameters.

    Falls back to English if the key is not found in the current locale.
    Falls back to the key itself if not found in English either.
    """
    messages = _load_locale(_current_locale)
    text = messages.get(key)
    if text is None:
        fallback = _load_locale(DEFAULT_LOCALE)
        text = fallback.get(key, key)
    if kwargs:
        text = text.format(**kwargs)
    return text
