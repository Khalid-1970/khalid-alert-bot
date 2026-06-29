import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

TARGET_PRICE = float(os.getenv("TARGET_PRICE", "0.0000000017"))

CONTRACT_ADDRESS = os.getenv(
    "CONTRACT_ADDRESS",
    "x95HN3DWvbfCBtTjGm587z8suK3ec6cwQwgZNLbWKyp"
)

CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "30"))

DEXSCREENER_API = (
    "https://api.dexscreener.com/latest/dex/tokens/"
    + CONTRACT_ADDRESS
)
