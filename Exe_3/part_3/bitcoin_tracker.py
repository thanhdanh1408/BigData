# import requests, time, datetime

# URL = "https://api.coingecko.com/api/v3/simple/price"
# PARAMS = {"ids": "bitcoin", "vs_currencies": "usd"}
# HEADERS = {"User-Agent": "Mozilla/5.0"} # tránh bị chặn bởi một số server

# def fetch_price():
#     r = requests.get(URL, params=PARAMS, headers=HEADERS, timeout=10)
#     r.raise_for_status()
#     data = r.json()
#     return data["bitcoin"]["usd"]

# while True:
#     try:
#         price = fetch_price()
#         ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         line = f"[{ts}] Giá Bitcoin (USD): {price}\n"
#         with open("bitcoin_price.txt", "a", encoding="utf-8") as f:
#             f.write(line)
#         print("💰", line.strip())

#     except Exception as e:
#         print("❌ Lỗi:", e)
#     time.sleep(30) # 30s là hợp lý với cache của API


import requests
import time
import datetime
import os
import pandas as pd

OUTPUT_DIR = "Exe_3/part_3/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

URL = "https://api.coingecko.com/api/v3/simple/price"
PARAMS = {"ids": "bitcoin", "vs_currencies": "usd"}
HEADERS = {"User-Agent": "Mozilla/5.0"}

csv_file = os.path.join(OUTPUT_DIR, "bitcoin_price.csv")
txt_file = os.path.join(OUTPUT_DIR, "bitcoin_price.txt")

if not os.path.exists(csv_file):
    pd.DataFrame(columns=["time", "price"]).to_csv(csv_file, index=False, encoding="utf-8-sig")

def fetch_price():
    r = requests.get(URL, params=PARAMS, headers=HEADERS, timeout=10)
    r.raise_for_status()
    data = r.json()
    return data["bitcoin"]["usd"]

while True:
    try:
        price = fetch_price()
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{ts}] Giá Bitcoin (USD): {price}"

        with open(txt_file, "a", encoding="utf-8") as f:
            f.write(line + "\n")

        df = pd.DataFrame([[ts, price]], columns=["time", "price"])
        df.to_csv(csv_file, mode="a", header=False, index=False, encoding="utf-8-sig")

        print("💰", line)

    except Exception as e:
        print("❌ Lỗi:", e)

    time.sleep(30)
