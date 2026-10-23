import sys
import os

# เพิ่มไดเรกทอรี 'src' เข้าไปใน Python path เพื่อให้เรียกใช้ตัว scraper ได้ถูกต้อง
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from scraper import SimpleWebScraper

def main():
    target_url = "https://automatetheboringstuff.com/3e/"
    scraper = SimpleWebScraper(target_url)

    scraped_data = scraper.scrape_main_titles()

    if scraped_data:
        print("\n--- ข้อมูลที่ Scrape ได้ ---")
        print(f"ชื่อหนังสือ: {scraped_data['book_title']}")
        print("\nชื่อบทต่างๆ:")
        if scraped_data['chapter_titles']:
            for i, title in enumerate(scraped_data['chapter_titles']):
                print(f"{i+1}. {title}")
        else:
            print("ไม่พบชื่อบทใดๆ")
        print("--------------------")
    else:
        print("ไม่สามารถ scrape ข้อมูลได้")

if __name__ == "__main__":
    main()
