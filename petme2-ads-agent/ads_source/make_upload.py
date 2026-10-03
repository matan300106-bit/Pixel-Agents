"""Guardian only: turn approved changes (JSON) into ONE bulk upload file in outbox/.

Run: python -m ads_source.make_upload outbox/YYYY-MM-DD/approved-changes.json

The JSON is a list of changes, for example:
  {"entity": "Keyword", "operation": "Update", "campaign_id": "1", "ad_group_id": "2",
   "keyword_id": "3", "bid": 0.85, "before": "bid 1.05", "reason": "ACOS 60% > target 30%",
   "agent": "optimizer"}

This script only WRITES A FILE. It does not upload anything.
"""
import json
import sys
from datetime import date
from pathlib import Path

from . import PROJECT_ROOT, get_source, load_settings

ALLOWED_OPERATIONS = {"create", "update", "archive"}


def _num(v):
    try:
        return float(str(v).rstrip("%"))
    except (TypeError, ValueError):
        return None


def check(changes, settings):
    """Return a list of problems. Empty list = OK to write the file."""
    problems = []
    if settings.get("mode") == "audit":
        problems.append("Mode is 'audit' (read only). No changes allowed.")
    limit = _num(settings.get("max_changes_per_day"))
    if limit is not None and len(changes) > limit:
        problems.append(f"{len(changes)} changes is more than max_changes_per_day ({int(limit)}).")
    max_bid = _num(settings.get("max_bid"))
    for i, c in enumerate(changes, 1):
        op = str(c.get("operation", "")).lower()
        if op not in ALLOWED_OPERATIONS:
            problems.append(f"#{i}: operation '{c.get('operation')}' is not allowed (never delete).")
        if op == "archive" and not c.get("owner_approved"):
            problems.append(f"#{i}: archive needs owner approval.")
        if op == "create" and str(c.get("entity", "")).lower() == "campaign":
            if str(c.get("state", "")).lower() != "paused" and not c.get("owner_approved"):
                problems.append(f"#{i}: new campaigns must be created PAUSED unless the owner approved.")
        bid = _num(c.get("bid"))
        if bid is not None and max_bid is not None and bid > max_bid and not c.get("owner_approved"):
            problems.append(f"#{i}: bid {bid} is above max_bid {max_bid}.")
    return problems


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    changes = json.loads(Path(sys.argv[1]).read_text())
    settings = load_settings()
    problems = check(changes, settings)
    if problems:
        print("BLOCKED - no file written:")
        for p in problems:
            print("  - " + p)
        return 1
    day = date.today().isoformat()
    clean = [{k: v for k, v in c.items() if k not in ("before", "reason", "agent", "owner_approved")}
             for c in changes]
    path = get_source(settings).prepare_changes(clean, day)
    print(f"Bulk upload file ready: {Path(path).relative_to(PROJECT_ROOT)} ({len(changes)} changes).")
    print("Upload it ONLY after the owner says APPROVED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
