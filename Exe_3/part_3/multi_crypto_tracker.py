import requests
import time
import datetime
import os
import pandas as pd

OUTPUT_DIR = "Exe_3/part_3/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

URL = "https://api.coingecko.com/api/v3/simple/price"
COINS = ["bitcoin", "ethereum", "dogecoin"]
PARAMS = {"ids": ",".join(COINS), "vs_currencies": "usd"}
HEADERS = {"User-Agent": "Mozilla/5.0"}

csv_file = os.path.join(OUTPUT_DIR, "crypto_prices.csv")

ALERTS = {
    "bitcoin": 70000,
    "ethereum": 4000,
    "dogecoin": 0.5
}

if not os.path.exists(csv_file):
    columns = ["time"] + [coin+"_usd" for coin in COINS]
    pd.DataFrame(columns=columns).to_csv(csv_file, index=False, encoding="utf-8-sig")

def fetch_prices():
    r = requests.get(URL, params=PARAMS, headers=HEADERS, timeout=10)
    r.raise_for_status()
    return r.json()

while True:
    try:
        data = fetch_prices()
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        row = {"time": ts}
        for coin in COINS:
            price = data[coin]["usd"]
            row[coin+"_usd"] = price

            print(f"[{ts}] {coin.upper()}: {price} USD")

            if coin in ALERTS and price >= ALERTS[coin]:
                print(f"⚠️ CẢNH BÁO: {coin.upper()} vượt ngưỡng {ALERTS[coin]} USD!")

        df = pd.DataFrame([row])
        df.to_csv(csv_file, mode="a", header=False, index=False, encoding="utf-8-sig")

    except Exception as e:
        print("❌ Lỗi:", e)

    time.sleep(30)
