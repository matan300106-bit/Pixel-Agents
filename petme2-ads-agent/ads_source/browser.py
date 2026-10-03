"""Ads source that uses the website (advertising.amazon.com) through Claude in Chrome.

Python cannot click in the browser. Claude (the Collector / Guardian) does the clicking,
following docs/how-to-download-reports.md, and saves files into inbox/YYYY-MM-DD/.
This class reads those files and writes the bulk upload file into outbox/YYYY-MM-DD/.
"""
from .base import AdsSource
from .files import detect_kind, read_sheets, split_bulk, write_bulk_upload

FILE_TYPES = (".xlsx", ".csv", ".tsv", ".txt")
EXPECTED = ("bulk", "search_terms", "targeting", "campaigns")


class BrowserAdsSource(AdsSource):
    name = "browser"

    def files(self, day=None):
        folder = self.inbox(day)
        if not folder.exists():
            return []
        return sorted(p for p in folder.iterdir() if p.suffix.lower() in FILE_TYPES)

    def fetch(self, day=None):
        files = self.files(day)
        if not files:
            raise FileNotFoundError(
                f"No ads files in {self.inbox(day)}. Download them in the browser first "
                "(see docs/how-to-download-reports.md)."
            )
        return files

    def missing(self, day=None):
        """Which expected files are not in the inbox yet."""
        found = {detect_kind(p, read_sheets(p)) for p in self.files(day)}
        return [k for k in EXPECTED if k not in found]

    def load(self, day=None):
        data = {}
        for path in self.fetch(day):
            sheets = read_sheets(path)
            kind = detect_kind(path, sheets)
            if kind == "bulk":
                for slug, rows in split_bulk(sheets).items():
                    data.setdefault(slug, []).extend(rows)
            else:
                for rows in sheets.values():
                    data.setdefault(kind, []).extend(rows)
        return data

    def prepare_changes(self, changes, day=None):
        return write_bulk_upload(changes, self.outbox(day) / "bulk-upload.xlsx")

    def apply(self, prepared):
        raise RuntimeError(
            "Upload is done in the browser by Guardian, only after the owner says APPROVED: "
            f"advertising.amazon.com > Bulk operations > upload {prepared}"
        )
