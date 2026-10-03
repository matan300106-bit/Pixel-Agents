"""Read the ads files in inbox/DAY/ and save clean CSV files in data/DAY/ads/.

Run: python -m ads_source.import_day [YYYY-MM-DD]
"""
import sys
from datetime import date

from . import PROJECT_ROOT, get_source
from .files import write_csv


def main():
    day = sys.argv[1] if len(sys.argv) > 1 else date.today().isoformat()
    source = get_source()
    try:
        data = source.load(day)
    except FileNotFoundError as e:
        print(f"Not ready: {e}")
        return 1

    out = PROJECT_ROOT / "data" / day / "ads"
    print(f"Ads files for {day}:")
    for name, rows in sorted(data.items()):
        write_csv(rows, out / f"{name}.csv")
        print(f"  {name}: {len(rows)} rows")
    missing = source.missing(day) if hasattr(source, "missing") else []
    if missing:
        print("Missing files: " + ", ".join(missing))
    print(f"Saved to data/{day}/ads/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
