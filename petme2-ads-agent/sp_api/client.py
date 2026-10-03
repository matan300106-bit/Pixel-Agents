"""Small READ-ONLY client for the Selling Partner API (North America, US).

Only GET requests are allowed, plus POST to a short list of endpoints that
only calculate something (fee estimates). Nothing here can change the account.
"""
import re
import time

import requests

from .auth import get_access_token

ENDPOINT = "https://sellingpartnerapi-na.amazon.com"
MARKETPLACE_ID = "ATVPDKIKX0DER"  # amazon.com (US)

# POST endpoints that do not change anything (they only return an estimate).
READ_ONLY_POST = [re.compile(r"^/products/fees/v0/items/[^/]+/feesEstimate$")]


class SpApiError(RuntimeError):
    pass


def _check_read_only(method, path):
    if method == "GET":
        return
    if method == "POST" and any(p.match(path) for p in READ_ONLY_POST):
        return
    raise SpApiError(f"Blocked: {method} {path} is not a read-only call.")


def call(method, path, params=None, body=None, max_tries=6):
    """Call SP-API and return the JSON body. Retries when Amazon says 'too fast'."""
    method = method.upper()
    _check_read_only(method, path)
    for attempt in range(max_tries):
        resp = requests.request(
            method,
            ENDPOINT + path,
            params=params,
            json=body,
            headers={
                "x-amz-access-token": get_access_token(),
                "user-agent": "petme2-ads-agent/1.0 (Language=Python)",
                "accept": "application/json",
            },
            timeout=60,
        )
        if resp.status_code == 429 or resp.status_code >= 500:
            time.sleep(min(2 ** attempt, 30))
            continue
        if resp.status_code >= 400:
            raise SpApiError(f"{method} {path} failed (HTTP {resp.status_code}): {resp.text[:500]}")
        return resp.json() if resp.content else {}
    raise SpApiError(f"{method} {path}: Amazon kept saying 'too many requests'. Try again later.")


def get(path, **params):
    return call("GET", path, params=params or None)
