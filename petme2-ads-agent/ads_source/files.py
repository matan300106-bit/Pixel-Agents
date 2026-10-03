"""Read Amazon Ads files (bulk file + reports) and write bulk upload files."""
import csv
import re
from pathlib import Path

from openpyxl import Workbook, load_workbook

SP_SHEET = "Sponsored Products Campaigns"

# Report column names differ between files. Map them to one clean name.
ALIASES = {
    "customer_search_term": "search_term",
    "7_day_total_sales": "sales",
    "14_day_total_sales": "sales",
    "7_day_total_orders": "orders",
    "14_day_total_orders": "orders",
    "7_day_total_units": "units",
    "14_day_total_units": "units",
    "7_day_conversion_rate": "conversion_rate",
    "total_advertising_cost_of_sales_acos": "acos",
    "total_return_on_advertising_spend_roas": "roas",
    "click_through_rate_ctr": "ctr",
    "click_through_rate": "ctr",
    "cost_per_click_cpc": "cpc",
}

NUMERIC = {"impressions", "clicks", "spend", "sales", "orders", "units", "cpc", "ctr",
           "acos", "roas", "conversion_rate", "bid", "daily_budget", "percentage",
           "ad_group_default_bid"}


def clean_header(h):
    h = re.sub(r"\(informational only\)", "", str(h or ""), flags=re.I)
    h = re.sub(r"[^a-z0-9]+", "_", h.lower()).strip("_")
    return ALIASES.get(h, h)


def to_number(v):
    if v is None or v == "":
        return None
    if isinstance(v, (int, float)):
        return v
    s = str(v).replace("$", "").replace(",", "").strip()
    pct = s.endswith("%")
    try:
        n = float(s.rstrip("%"))
    except ValueError:
        return v
    return n / 100 if pct else n


def _rows(header, values):
    keys = [clean_header(h) for h in header]
    out = []
    for vals in values:
        if not any(v not in (None, "") for v in vals):
            continue
        row = {}
        for k, v in zip(keys, vals):
            if not k or (k in row and row[k] not in (None, "")):
                continue  # keep first non-empty when two columns clean to the same name
            row[k] = to_number(v) if k in NUMERIC else v
        out.append(row)
    return out


def read_sheets(path):
    """Return {sheet_name: [row dicts]} for .xlsx or {"report": rows} for .csv/.tsv."""
    path = Path(path)
    if path.suffix.lower() in (".csv", ".tsv", ".txt"):
        with open(path, newline="", encoding="utf-8-sig") as f:
            sample = f.read(4096)
            f.seek(0)
            delim = "\t" if sample.count("\t") > sample.count(",") else ","
            data = list(csv.reader(f, delimiter=delim))
        return {"report": _rows(data[0], data[1:])} if data else {}
    wb = load_workbook(path, read_only=True, data_only=True)
    sheets = {}
    for ws in wb.worksheets:
        values = list(ws.iter_rows(values_only=True))
        if values:
            sheets[ws.title] = _rows(values[0], values[1:])
    wb.close()
    return sheets


def detect_kind(path, sheets):
    """Guess what kind of file this is: bulk, search_terms, targeting, placement, campaigns."""
    if any(SP_SHEET.lower() in name.lower() for name in sheets):
        return "bulk"
    first = next(iter(sheets.values()), [])
    cols = set(first[0]) if first else set()
    name = Path(path).name.lower()
    if "search_term" in cols or "search_term" in name or "search term" in name:
        return "search_terms"
    if "placement" in cols or "placement" in name:
        return "placement"
    if "targeting" in cols or "targeting" in name:
        return "targeting"
    return "campaigns"


def split_bulk(sheets):
    """Split the bulk file into {entity_slug: rows}, e.g. 'keyword', 'campaign', 'sp_search_terms'."""
    out = {}
    for name, rows in sheets.items():
        if "search term" in name.lower():
            out.setdefault(re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_"), []).extend(rows)
            continue
        if "portfolio" in name.lower() or not rows or "entity" not in rows[0]:
            continue
        prefix = "sp_" if name == SP_SHEET else re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_") + "__"
        for r in rows:
            slug = prefix + re.sub(r"[^a-z0-9]+", "_", str(r.get("entity") or "").lower()).strip("_")
            out.setdefault(slug, []).append(r)
    return out


def write_csv(rows, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(dict.fromkeys(k for r in rows for k in r))
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


# ---- bulk upload file ---------------------------------------------------

UPLOAD_COLUMNS = [
    ("Product", "product"), ("Entity", "entity"), ("Operation", "operation"),
    ("Campaign ID", "campaign_id"), ("Ad Group ID", "ad_group_id"), ("Portfolio ID", "portfolio_id"),
    ("Ad ID", "ad_id"), ("Keyword ID", "keyword_id"), ("Product Targeting ID", "product_targeting_id"),
    ("Campaign Name", "campaign_name"), ("Ad Group Name", "ad_group_name"),
    ("Start Date", "start_date"), ("End Date", "end_date"), ("Targeting Type", "targeting_type"),
    ("State", "state"), ("Daily Budget", "daily_budget"), ("SKU", "sku"),
    ("Ad Group Default Bid", "ad_group_default_bid"), ("Bid", "bid"),
    ("Keyword Text", "keyword_text"), ("Match Type", "match_type"),
    ("Bidding Strategy", "bidding_strategy"), ("Placement", "placement"), ("Percentage", "percentage"),
    ("Product Targeting Expression", "product_targeting_expression"),
]


def write_bulk_upload(changes, path):
    """Write one Sponsored Products bulk upload file (.xlsx) from a list of change dicts."""
    wb = Workbook()
    ws = wb.active
    ws.title = SP_SHEET
    ws.append([title for title, _ in UPLOAD_COLUMNS])
    for c in changes:
        c = {"product": "Sponsored Products", **c}
        ws.append([c.get(key) for _, key in UPLOAD_COLUMNS])
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)
    return path
