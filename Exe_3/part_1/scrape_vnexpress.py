# import requests
# from bs4 import BeautifulSoup

# url = "https://vnexpress.net/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# titles = soup.find_all("h3", class_="title-news")

# with open("baiviet.txt", "w", encoding="utf-8") as f:
#     for t in titles:
#         f.write(t.get_text(strip=True) + "\n")
# print("✅ Đã lưu tiêu đề vào file baiviet.txt")


import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

OUTPUT_DIR = "Exe_3/part_1/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def scrape_vnexpress_homepage():
    url = "https://vnexpress.net/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article", class_="item-news")
    data = []
    for a in articles:
        title_tag = a.find("h3", class_="title-news")
        summary_tag = a.find("p", class_="description")

        title = title_tag.get_text(strip=True) if title_tag else None
        link = title_tag.a["href"] if title_tag and title_tag.a else None
        summary = summary_tag.get_text(strip=True) if summary_tag else None

        if title:
            data.append({"title": title, "summary": summary, "link": link})

    df = pd.DataFrame(data)
    output_path = os.path.join(OUTPUT_DIR, "vnexpress.csv")
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"✅ Đã lưu {len(df)} bài viết vào {output_path}")

if __name__ == "__main__":
    scrape_vnexpress_homepage()
