#!/usr/bin/env python3
"""Helium 10 Listing Builder-style keyword score for the PETME2 feeder listings.

Score per product, using keyword-banks.json -> [asin].top60 (black B0GHMCG8Q9 and
parent B0H3L6VXV6 use the B0GHLSQMJ9 bank):

  weighted  = sum(sv * w) / sum(sv), w = 1.0 if the keyword is an exact phrase in the
              title, else 0.8 if in a bullet, else 0.5 if in the description, else 0
  exact     = share of volume used as an exact phrase in title + bullets + description
  indexed   = share of volume whose words all appear somewhere (title, bullets,
              description, backend)

Exact phrase = case-insensitive, whole words, words separated only by spaces
(punctuation between words breaks the phrase). Also checks the listing rules.

Usage: python3 score.py [listings.json] [ASIN ...]
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SEO = os.path.dirname(HERE)
FEEDERS = ["B0GHLSQMJ9", "B0GHMCG8Q9", "B0H3L6VXV6", "B0GHH8L59K", "B0GTCGYZDM"]
BANK_ALIAS = {"B0GHMCG8Q9": "B0GHLSQMJ9", "B0H3L6VXV6": "B0GHLSQMJ9"}
STOP = {"a", "an", "the", "and", "or", "for", "with", "to", "of", "in", "on", "&"}
BANNED_CHARS = set("!$?_{}^¬¦")
PROMO = ["best", "top", "#1", "perfect", "ideal", "premium", "luxury", "easiest"]
HEALTH = ["antibacterial", "anti-bacterial", "hygienic", "hygiene", "bacteria", "germ",
          "healthy", "healthier", "cure", "prevent disease", "chin acne", "vet"]
EMOJI = re.compile("[\U0001F000-\U0001FFFF☀-➿⬀-⯿️]")


def norm(text):
    return " " + re.sub(r"\s+", " ", text.lower()) + " "


def has_phrase(text, kw):
    return re.search(r"(?<![a-z0-9])" + re.escape(kw.lower()) + r"(?![a-z0-9])", norm(text)) is not None


def tokens(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def bank_for(asin, banks):
    return banks[BANK_ALIAS.get(asin, asin)]["top60"]


def score(entry, top60):
    title, bullets, desc = entry["title"], " \n ".join(entry["bullets"]), entry["description"]
    backend = entry.get("backend", "")
    alltok = tokens(" ".join([title, bullets, desc, backend]))
    total = sum(k["sv"] for k in top60)
    w = ex = ix = 0
    missing, unindexed = [], []
    for k in top60:
        kw, sv = k["kw"], k["sv"]
        if has_phrase(title, kw):
            wt = 1.0
        elif any(has_phrase(b, kw) for b in entry["bullets"]):
            wt = 0.8
        elif has_phrase(desc, kw):
            wt = 0.5
        else:
            wt = 0
            missing.append((kw, sv))
        w += sv * wt
        ex += sv if wt else 0
        if set(re.findall(r"[a-z0-9]+", kw.lower())) <= alltok:
            ix += sv
        else:
            unindexed.append((kw, sv))
    return {"weighted": 100 * w / total, "exact": 100 * ex / total, "indexed": 100 * ix / total,
            "missing": missing, "unindexed": unindexed}


def stem(word):
    return word[:-1] if len(word) > 3 and word.endswith("s") and not word.endswith("ss") else word


def check_rules(entry):
    errs = []
    title = entry["title"]
    if len(title) > 200:
        errs.append(f"title {len(title)} chars > 200")
    counts = {}
    for t in re.findall(r"[a-z0-9#&'-]+", title.lower()):
        if t in STOP:
            continue
        counts[stem(t)] = counts.get(stem(t), 0) + 1
    over = {k: v for k, v in counts.items() if v > 2}
    if over:
        errs.append(f"title words >2x: {over}")
    texts = [("title", title), ("description", entry["description"])] + \
            [(f"bullet{i+1}", b) for i, b in enumerate(entry["bullets"])]
    for name, t in texts:
        bad = BANNED_CHARS & set(t)
        if bad:
            errs.append(f"{name}: banned chars {sorted(bad)}")
        if EMOJI.search(t):
            errs.append(f"{name}: emoji")
        low = t.lower()
        for p in PROMO:
            if re.search(r"(?<![a-z0-9])" + re.escape(p) + r"(?![a-z0-9])", low):
                errs.append(f"{name}: promo word '{p}'")
        for h in HEALTH:
            if h in low:
                errs.append(f"{name}: health claim '{h}'")
    if len(entry["bullets"]) != 5:
        errs.append(f"{len(entry['bullets'])} bullets (need 5)")
    for i, b in enumerate(entry["bullets"]):
        if len(b) > 500:
            errs.append(f"bullet{i+1} {len(b)} chars > 500")
    if len(entry["description"]) > 2000:
        errs.append(f"description {len(entry['description'])} chars > 2000")
    be = entry.get("backend", "")
    if len(be.encode("utf-8")) > 249:
        errs.append(f"backend {len(be.encode('utf-8'))} bytes > 249")
    clash = sorted({t for t in tokens(be) if t in tokens(title) or stem(t) in {stem(x) for x in tokens(title)}})
    if clash:
        errs.append(f"backend repeats title words: {clash}")
    if "petme2" in be.lower():
        errs.append("backend contains brand")
    return errs


def main():
    args = sys.argv[1:]
    path = os.path.join(HERE, "listings-final.json")
    if args and args[0].endswith(".json"):
        path = args.pop(0)
    asins = args or FEEDERS
    listings = json.load(open(path))
    banks = json.load(open(os.path.join(SEO, "keyword-banks.json")))
    for a in asins:
        e = listings[a]
        s = score(e, bank_for(a, banks))
        print(f"=== {a} {e.get('product', '')}")
        print(f"  weighted {s['weighted']:.1f}% | exact (title+bullets+desc) {s['exact']:.1f}% | indexed {s['indexed']:.1f}%")
        print(f"  title {len(e['title'])}c, bullets {[len(b) for b in e['bullets']]}, desc {len(e['description'])}c, backend {len(e.get('backend','').encode())}B")
        errs = check_rules(e)
        print("  rules: " + ("OK" if not errs else "FAIL -> " + "; ".join(errs)))
        if s["missing"]:
            print("  not used as exact phrase (by volume):")
            for kw, sv in sorted(s["missing"], key=lambda x: -x[1]):
                print(f"    {sv:>7}  {kw}")
        if s["unindexed"]:
            print("  not indexed: " + ", ".join(f"{k} ({v})" for k, v in s["unindexed"]))


if __name__ == "__main__":
    main()
