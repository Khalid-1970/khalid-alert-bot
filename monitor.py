import time

from config import TARGET_PRICE, CHECK_INTERVAL
from dexscreener import get_token_data
from alerts import send_message

alert_sent = False


def start_monitor():

    global alert_sent

    print("Monitoring started...")

    while True:

        token = get_token_data()

        if token:

            price = token["price_usd"]

            print(price)

            if price >= TARGET_PRICE and not alert_sent:

                message = f"""
🚨 *TARGET PRICE REACHED*

Price: ${price}

Target: ${TARGET_PRICE}

24H Change: {token['price_change_24h']}%

Liquidity: ${token['liquidity_usd']}

Volume: ${token['volume_24h']}

Dex: {token['dex']}

Chart:
{token['url']}
"""

                send_message(message)

                alert_sent = True

        time.sleep(CHECK_INTERVAL)
