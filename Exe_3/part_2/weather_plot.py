import pandas as pd
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = "Exe_3/part_2/output"
input_csv = os.path.join(OUTPUT_DIR, "weather_multiple.csv")

def plot_weather(city="Hà Nội"):
    df = pd.read_csv(input_csv)
    city_df = df[df["city"] == city]

    plt.figure(figsize=(12, 5))
    plt.plot(city_df["time"], city_df["temperature"], marker="o", label="Nhiệt độ (°C)")
    plt.plot(city_df["time"], city_df["humidity"], marker="x", label="Độ ẩm (%)")
    plt.plot(city_df["time"], city_df["wind"], marker="s", label="Gió (m/s)")

    plt.title(f"Thời tiết {city}")
    plt.xlabel("Thời gian (UTC)")
    plt.ylabel("Giá trị")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_weather("Hà Nội")
