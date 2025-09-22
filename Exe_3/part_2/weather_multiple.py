import requests
import pandas as pd
import os

OUTPUT_DIR = "Exe_3/part_2/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

cities = {
    "Hà Nội": (21.0285, 105.8542),
    "TP.HCM": (10.7769, 106.7009),
    "Đà Nẵng": (16.0544, 108.2022)
}

def fetch_weather_multiple():
    all_data = []
    for city, (lat, lon) in cities.items():
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "hourly": "temperature_2m,relative_humidity_2m,windspeed_10m"
        }
        response = requests.get(url, params=params)
        data = response.json()

        df = pd.DataFrame({
            "time": data["hourly"]["time"],
            "temperature": data["hourly"]["temperature_2m"],
            "humidity": data["hourly"]["relative_humidity_2m"],
            "wind": data["hourly"]["windspeed_10m"],
            "city": city
        })
        all_data.append(df)

    final_df = pd.concat(all_data)
    output_csv = os.path.join(OUTPUT_DIR, "weather_multiple.csv")
    final_df.to_csv(output_csv, index=False, encoding="utf-8-sig")
    print(f"✅ Đã lưu dữ liệu thời tiết nhiều thành phố vào {output_csv}")

if __name__ == "__main__":
    fetch_weather_multiple()
