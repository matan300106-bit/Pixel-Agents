"""Validate templates/*.json against Dawn section schemas.
Usage: python3 validate_templates.py <dawn_dir> [template names...]"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).parent
DAWN = Path(sys.argv[1])
NAMES = sys.argv[2:] or ["collection", "list-collections", "cart", "search", "404", "page", "page.contact",
                         "password"]
SCHEMES = {f"scheme-{i}" for i in range(1, 6)}
SCHEMA_RE = re.compile(r"{%-?\s*schema\s*-?%}(.*?){%-?\s*endschema\s*-?%}", re.S)


def strip_comments(t):
    return re.sub(r"/\*.*?\*/", "", t, flags=re.S)


def schema(type_):
    p = DAWN / "sections" / f"{type_}.liquid"
    if not p.exists():
        p = HERE / "sections" / f"{type_}.liquid"
    if not p.exists():
        return None
    m = SCHEMA_RE.search(p.read_text())
    return json.loads(m.group(1)) if m else {}


def check_settings(where, values, defs, errs):
    by_id = {d["id"]: d for d in defs if "id" in d}
    for k, v in (values or {}).items():
        d = by_id.get(k)
        if not d:
            errs.append(f"{where}: unknown setting '{k}'"); continue
        t = d["type"]
        if t in ("select", "radio"):
            opts = [o["value"] for o in d["options"]]
            if v not in opts:
                errs.append(f"{where}.{k}: '{v}' not in {opts}")
        elif t == "range":
            if not isinstance(v, (int, float)) or isinstance(v, bool):
                errs.append(f"{where}.{k}: range needs number, got {v!r}")
            else:
                lo, hi, st = d["min"], d["max"], d.get("step", 1)
                if not lo <= v <= hi or (v - lo) % st:
                    errs.append(f"{where}.{k}: {v} outside {lo}-{hi} step {st}")
        elif t == "checkbox" and not isinstance(v, bool):
            errs.append(f"{where}.{k}: checkbox needs bool, got {v!r}")
        elif t == "color_scheme" and v not in SCHEMES:
            errs.append(f"{where}.{k}: unknown color scheme {v!r}")
        elif t == "richtext" and v and not re.match(r"^<(p|ul|ol|h[1-6])\b", v):
            errs.append(f"{where}.{k}: richtext must start with a block tag")
        elif t == "url" and v and not re.match(r"^(/|https?://|shopify://|mailto:|tel:|#)", v):
            errs.append(f"{where}.{k}: bad url {v!r}")
        elif t in ("text", "inline_richtext") and not isinstance(v, str):
            errs.append(f"{where}.{k}: expected string")


def default_main_types(name):
    t = json.loads(strip_comments((DAWN / "templates" / f"{name}.json").read_text()))
    return sorted(s["type"] for s in t["sections"].values() if s["type"].startswith("main-")), t.get("layout")


total = 0
for name in NAMES:
    errs = []
    tpl = json.loads((HERE / "templates" / f"{name}.json").read_text())
    secs = tpl["sections"]
    if sorted(tpl["order"]) != sorted(secs):
        errs.append("order does not match sections keys")
    mine = sorted(s["type"] for s in secs.values() if s["type"].startswith("main-"))
    dawn_main, dawn_layout = default_main_types(name)
    if mine != dawn_main:
        errs.append(f"main sections {mine} != Dawn default {dawn_main}")
    if tpl.get("layout") != dawn_layout:
        errs.append(f"layout {tpl.get('layout')!r} != Dawn default {dawn_layout!r}")
    for sid, s in secs.items():
        sc = schema(s["type"])
        if sc is None:
            errs.append(f"{sid}: section type '{s['type']}' not found"); continue
        check_settings(f"{sid}", s.get("settings"), sc.get("settings", []), errs)
        if "templates" in sc and name.split(".")[0] not in sc["templates"]:
            errs.append(f"{sid}: '{s['type']}' not enabled on template '{name}'")
        if "disabled_on" in sc and name.split(".")[0] in sc["disabled_on"].get("templates", []):
            errs.append(f"{sid}: '{s['type']}' disabled on '{name}'")
        blocks, order = s.get("blocks", {}), s.get("block_order", [])
        if sorted(order) != sorted(blocks):
            errs.append(f"{sid}: block_order does not match blocks")
        bdefs = {b["type"]: b for b in sc.get("blocks", [])}
        if blocks and not bdefs:
            errs.append(f"{sid}: section accepts no blocks")
        if sc.get("max_blocks") is not None and len(blocks) > sc["max_blocks"]:
            errs.append(f"{sid}: {len(blocks)} blocks > max_blocks {sc['max_blocks']}")
        counts = {}
        for bid, b in blocks.items():
            counts[b["type"]] = counts.get(b["type"], 0) + 1
            if b["type"].startswith("shopify://apps/") and "@app" in bdefs:
                continue
            bd = bdefs.get(b["type"])
            if not bd:
                errs.append(f"{sid}.{bid}: unknown block type '{b['type']}'"); continue
            check_settings(f"{sid}.{bid}", b.get("settings"), bd.get("settings", []), errs)
        for bt, n in counts.items():
            lim = bdefs.get(bt, {}).get("limit")
            if lim is not None and n > lim:
                errs.append(f"{sid}: {n} '{bt}' blocks > limit {lim}")
    total += len(errs)
    print(f"{name}.json: {'OK' if not errs else str(len(errs)) + ' error(s)'}")
    for e in errs:
        print("   -", e)
print(f"\n{total} error(s)")
sys.exit(1 if total else 0)
