import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

OUTPUT_DIR = "Exe_3/part_1/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def scrape_multiple_pages(pages=3):
    all_articles = []
    for page in range(1, pages + 1):
        url = f"https://vnexpress.net/?page={page}"
        print(f"🔎 Đang lấy dữ liệu từ trang {page}...")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.find_all("article", class_="item-news")
        for a in articles:
            title_tag = a.find("h3", class_="title-news")
            summary_tag = a.find("p", class_="description")

            title = title_tag.get_text(strip=True) if title_tag else None
            link = title_tag.a["href"] if title_tag and title_tag.a else None
            summary = summary_tag.get_text(strip=True) if summary_tag else None

            if title:
                all_articles.append({
                    "title": title,
                    "summary": summary,
                    "link": link,
                    "page": page
                })

    df = pd.DataFrame(all_articles)
    output_path = os.path.join(OUTPUT_DIR, "vnexpress_multi.csv")
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"✅ Đã lưu {len(df)} bài viết từ {pages} trang vào {output_path}")

if __name__ == "__main__":
    scrape_multiple_pages(3)
