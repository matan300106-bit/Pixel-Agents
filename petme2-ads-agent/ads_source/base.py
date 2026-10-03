"""The one swappable "ads source" layer.

Every agent gets ads data and sends ads changes ONLY through an AdsSource.
Today: BrowserAdsSource (files downloaded by Claude in Chrome).
Later: AdsApiSource (Amazon Ads API) - same methods, nothing else changes.
"""
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


class AdsSource:
    name = "base"

    def inbox(self, day=None):
        return PROJECT_ROOT / "inbox" / (day or date.today().isoformat())

    def outbox(self, day=None):
        return PROJECT_ROOT / "outbox" / (day or date.today().isoformat())

    def fetch(self, day=None):
        """Make sure today's ads files exist in inbox/DAY/. Return the list of files."""
        raise NotImplementedError

    def load(self, day=None):
        """Return {dataset_name: rows}, e.g. 'sp_keyword', 'sp_campaign', 'search_terms'."""
        raise NotImplementedError

    def prepare_changes(self, changes, day=None):
        """Turn approved changes into whatever this source needs (a bulk file for the browser)."""
        raise NotImplementedError

    def apply(self, prepared):
        """Send the changes to Amazon. Only after the owner said APPROVED."""
        raise NotImplementedError
