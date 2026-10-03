"""Get an SP-API access token, using the keys in .env.

Keys are read from .env only. They are never printed or logged.
"""
import os
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TOKEN_URL = "https://api.amazon.com/auth/o2/token"
REQUIRED_KEYS = ("LWA_CLIENT_ID", "LWA_CLIENT_SECRET", "SP_API_REFRESH_TOKEN")

_cache = {"token": None, "expires_at": 0.0}


class MissingKeysError(RuntimeError):
    pass


def load_keys():
    load_dotenv(PROJECT_ROOT / ".env")
    missing = [k for k in REQUIRED_KEYS if not os.getenv(k, "").strip()]
    if missing:
        raise MissingKeysError(
            "These keys are empty in .env: " + ", ".join(missing)
            + ". Open the .env file, type the values after '=', and save."
        )
    return {k: os.environ[k].strip() for k in REQUIRED_KEYS}


def get_access_token():
    """Return a valid access token (cached for ~1 hour)."""
    if _cache["token"] and time.time() < _cache["expires_at"] - 60:
        return _cache["token"]

    keys = load_keys()
    resp = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "refresh_token",
            "refresh_token": keys["SP_API_REFRESH_TOKEN"],
            "client_id": keys["LWA_CLIENT_ID"],
            "client_secret": keys["LWA_CLIENT_SECRET"],
        },
        timeout=30,
    )
    if resp.status_code != 200:
        try:
            info = resp.json()
            reason = f"{info.get('error')}: {info.get('error_description')}"
        except ValueError:
            reason = "no details"
        raise RuntimeError(f"Amazon login failed (HTTP {resp.status_code}) - {reason}")

    body = resp.json()
    _cache["token"] = body["access_token"]
    _cache["expires_at"] = time.time() + int(body.get("expires_in", 3600))
    return _cache["token"]
