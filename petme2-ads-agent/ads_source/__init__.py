"""Swappable ads data layer. Use get_source() - never talk to Amazon Ads directly."""
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_settings():
    with open(PROJECT_ROOT / "settings.yaml") as f:
        return yaml.safe_load(f) or {}


def get_source(settings=None):
    settings = settings or load_settings()
    kind = settings.get("ads_source", "browser")
    if kind == "browser":
        from .browser import BrowserAdsSource
        return BrowserAdsSource()
    if kind == "ads_api":
        from .ads_api import AdsApiSource
        return AdsApiSource()
    raise ValueError(f"Unknown ads_source in settings.yaml: {kind}")
