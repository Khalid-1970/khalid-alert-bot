import requests
from config import DEXSCREENER_API


def get_token_data():
    """
    Fetch token information from DexScreener.
    Returns a dictionary or None if unavailable.
    """
    try:
        response = requests.get(DEXSCREENER_API, timeout=15)
        response.raise_for_status()

        data = response.json()

        pairs = data.get("pairs", [])

        if not pairs:
            return None

        pair = pairs[0]

        return {
            "price_usd": float(pair.get("priceUsd", 0)),
            "price_native": pair.get("priceNative"),
            "fdv": pair.get("fdv"),
            "market_cap": pair.get("marketCap"),
            "liquidity_usd": pair.get("liquidity", {}).get("usd"),
            "volume_24h": pair.get("volume", {}).get("h24"),
            "price_change_24h": pair.get("priceChange", {}).get("h24"),
            "dex": pair.get("dexId"),
            "pair_address": pair.get("pairAddress"),
            "url": pair.get("url"),
            "base_token": pair.get("baseToken", {}).get("symbol"),
            "quote_token": pair.get("quoteToken", {}).get("symbol"),
        }

    except Exception as e:
        print(f"DexScreener Error: {e}")
        return None
