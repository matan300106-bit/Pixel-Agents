#!/usr/bin/env python3
"""Helium 10 Listing Builder-style keyword score for the PETME2 fountain listings.

Per product, using research/seo/keyword-banks.json -> [asin].top60:
  weighted  = sum(sv * w) / total_sv, w = 1.0 if exact phrase in title,
              else 0.8 if in bullets, else 0.5 if in description, else 0
  exact     = share of sv where the keyword is an exact phrase (case-insensitive,
              word-bounded) in title, bullets or description
  indexed   = share of sv where every word of the keyword appears anywhere
              (title + bullets + description + backend)
Usage: score-fountains.py [listings.json] [--missing N]
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FOUNTAINS = ["B0DR7FCLZR", "B0GHKN9DBR", "B0GHLBGCP3", "B0GHKRYV6W"]


def norm(s):
    return " " + re.sub(r"[^a-z0-9]+", " ", s.lower()).strip() + " "


def has_phrase(text_n, kw):
    return norm(kw) in text_n


def words(text_n):
    return set(text_n.split())


def score(entry, top60):
    t = norm(entry["title"]); b = norm(" ".join(entry["bullets"])); d = norm(entry["description"])
    allw = words(t) | words(b) | words(d) | words(norm(entry.get("backend", "")))
    total = sum(k["sv"] for k in top60) or 1
    wsum = exact = idx = 0
    missing, unindexed = [], []
    for k in top60:
        kw, sv = k["kw"], k["sv"]
        w = 1.0 if has_phrase(t, kw) else 0.8 if has_phrase(b, kw) else 0.5 if has_phrase(d, kw) else 0
        wsum += sv * w
        if w: exact += sv
        else: missing.append((sv, kw))
        if set(norm(kw).split()) <= allw: idx += sv
        else: unindexed.append((sv, kw))
    return {"weighted": 100 * wsum / total, "exact": 100 * exact / total, "indexed": 100 * idx / total,
            "missing": sorted(missing, reverse=True), "unindexed": sorted(unindexed, reverse=True)}


def main():
    args = sys.argv[1:]
    n = 60
    if "--missing" in args:
        i = args.index("--missing"); n = int(args[i + 1]); del args[i:i + 2]
    path = Path(args[0]) if args else HERE / "listings-final.json"
    listings = json.loads(path.read_text())
    banks = json.loads((HERE.parent / "keyword-banks.json").read_text())
    for asin in FOUNTAINS:
        s = score(listings[asin], banks[asin]["top60"])
        print(f"== {asin} {listings[asin].get('product','')}")
        print(f"   weighted {s['weighted']:.1f}%  exact(T+B+D) {s['exact']:.1f}%  indexed {s['indexed']:.1f}%")
        for sv, kw in s["missing"][:n]:
            print(f"     not exact: {sv:>7}  {kw}")
        for sv, kw in s["unindexed"]:
            print(f"     NOT INDEXED: {sv:>7}  {kw}")


if __name__ == "__main__":
    main()
