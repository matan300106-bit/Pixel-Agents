"""Write site-state.json (what petme2.com/pages/cat-town shows) from the latest episode.json."""
import json
from pathlib import Path
HERE = Path(__file__).parent
ep = json.loads((HERE / "episode.json").read_text())
keep = lambda d, ks: {k: d[k] for k in ks if k in d}
site = {
    "day": ep["day"], "islandRadius": ep["islandRadius"], "trees": ep["trees"],
    "houses": [keep(h, ["x", "z", "ry", "roof", "wall", "day"]) for h in ep["houses"]],
    "buildings": [keep(b, ["kind", "x", "z", "ry", "sign", "day", "by", "request"]) for b in ep["buildings"]],
    "cats": [keep(c, ["x", "z", "color"]) for c in ep["cats"]],
}
(HERE / "site-state.json").write_text(json.dumps(site, separators=(",", ":")))
print(len(json.dumps(site)), "bytes;", len(site["houses"]), "houses,", len(site["buildings"]), "buildings")
