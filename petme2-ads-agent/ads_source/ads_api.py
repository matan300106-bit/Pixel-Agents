"""Placeholder for the Amazon Ads API source (not used yet).

When the owner gets Ads API access, implement the same methods as BrowserAdsSource:
fetch() -> request reports, load() -> same dataset names, prepare_changes() -> API payloads,
apply() -> send them. Then set `ads_source: ads_api` in settings.yaml. No agent needs to change.
"""
from .base import AdsSource


class AdsApiSource(AdsSource):
    name = "ads_api"

    def __init__(self):
        raise NotImplementedError("Ads API is not set up yet. Use ads_source: browser in settings.yaml.")
