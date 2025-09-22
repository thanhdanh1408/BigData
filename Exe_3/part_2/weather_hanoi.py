# import requests
# import pandas as pd

# url = "https://api.open-meteo.com/v1/forecast"
# params = {
#     "latitude": 21.0285, # Hà Nội
#     "longitude": 105.8542,
#     "hourly": "temperature_2m"
# }

# response = requests.get(url, params=params)
# data = response.json()

# df = pd.DataFrame({
#     "time": data["hourly"]["time"],
#     "temperature": data["hourly"]["temperature_2m"]
# })

# df.to_csv("weather.csv", index=False, encoding="utf-8")
# df.to_json("weather.json", orient="records", force_ascii=False)

# print("✅ Đã lưu dữ liệu thời tiết vào weather.csv và weather.json")


import requests
import pandas as pd
import os

OUTPUT_DIR = "Exe_3/part_2/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_weather_hanoi():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 21.0285,   # Hà Nội
        "longitude": 105.8542,
        "hourly": "temperature_2m"
    }

    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame({
        "time": data["hourly"]["time"],
        "temperature": data["hourly"]["temperature_2m"]
    })

    output_csv = os.path.join(OUTPUT_DIR, "weather_hanoi.csv")
    output_json = os.path.join(OUTPUT_DIR, "weather_hanoi.json")

    df.to_csv(output_csv, index=False, encoding="utf-8-sig")
    df.to_json(output_json, orient="records", force_ascii=False, indent=2)

    print(f"✅ Đã lưu dữ liệu Hà Nội vào {output_csv} và {output_json}")

if __name__ == "__main__":
    fetch_weather_hanoi()
