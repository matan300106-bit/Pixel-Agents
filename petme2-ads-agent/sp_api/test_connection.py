"""Test the SP-API keys. Run: python -m sp_api.test_connection"""
import sys

from .auth import MissingKeysError, get_access_token
from .client import get


def main():
    try:
        get_access_token()
        print("Step 1 OK: Amazon login worked (access token received).")
        data = get("/sellers/v1/marketplaceParticipations")
    except MissingKeysError as e:
        print(f"Not ready: {e}")
        return 1
    except Exception as e:  # noqa: BLE001 - show a simple message to the owner
        print(f"Problem: {e}")
        return 1

    print("Step 2 OK: SP-API answered. Your marketplaces:")
    for p in data.get("payload", []):
        m = p.get("marketplace", {})
        print(f"  - {m.get('name')} ({m.get('id')}, {m.get('countryCode')})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
