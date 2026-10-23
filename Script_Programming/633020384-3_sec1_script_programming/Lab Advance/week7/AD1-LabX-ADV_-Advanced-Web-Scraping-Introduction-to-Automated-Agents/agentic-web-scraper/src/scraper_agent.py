import requests
from bs4 import BeautifulSoup
import urllib.parse
import time

class ScraperAgent:
    def __init__(self, config: dict):
        # โหลดค่าคอนฟิกต่างๆ มาใช้งาน
        self.start_url = config.get("start_url")
        self.max_pages = config.get("max_pages", 1)
        self.delay = config.get("delay_between_pages", 0)
        self.container_selector = config.get("item_container_selector")
        self.selectors = config.get("item_data_selectors", {})

    def scrape_books(self):
        all_books = []
        current_page = 1

        while current_page <= self.max_pages:
            # คำนวณหา URL ของแต่ละหน้าเพจ (Pagination)
            if current_page == 1:
                url = self.start_url
            else:
                url = urllib.parse.urljoin(self.start_url, f"catalogue/page-{current_page}.html")

            # 📌 แสดงสถานะใน Terminal ตามหน้าจอที่คุณอยากได้
            print(f"Scraping page {current_page}...")

            try:
                headers = {'User-Agent': 'Mozilla/5.0'}
                response = requests.get(url, headers=headers)
                
                if response.status_code != 200:
                    break

                soup = BeautifulSoup(response.text, 'html.parser')
                # หาบล็อกกล่องสินค้าหลัก
                products = soup.select(self.container_selector)

                for prod in products:
                    # ดึงข้อมูลผ่าน Selector ที่ดึงมาจากตัวแปรคอนฟิก
                    name_tag = prod.select_one(self.selectors.get("name", "h3 a"))
                    name = name_tag.get('title') or name_tag.get_text(strip=True) if name_tag else "Unknown"

                    price_tag = prod.select_one(self.selectors.get("price", "p.price_color"))
                    price = price_tag.get_text(strip=True) if price_tag else None

                    # สกัดแกะ absolute URL ลิงก์สินค้า
                    full_url = self.start_url
                    if name_tag and name_tag.get('href'):
                        href = name_tag.get('href')
                        if href.startswith('catalogue/'):
                            full_url = urllib.parse.urljoin(self.start_url, href)
                        else:
                            full_url = urllib.parse.urljoin(self.start_url, f"catalogue/{href}")

                    # สกัดแกะ absolute URL รูปภาพสินค้า
                    img_tag = prod.select_one(self.selectors.get("image_url", "img.thumbnail"))
                    img_url = ""
                    if img_tag and img_tag.get('src'):
                        img_src = img_tag.get('src').replace('../', '')
                        img_url = urllib.parse.urljoin(self.start_url, img_src)

                    # โครงสร้าง JSON ที่ตรงกับรูปแบบที่คุณส่งมาในรูปภาพ
                    all_books.append({
                        "name": name,
                        "price": price,
                        "description": None,
                        "url": full_url,
                        "image_url": img_url
                    })

                # เว้นระยะเวลาการดาวน์โหลดตามคอนฟิกเพื่อความปลอดภัย
                if self.delay > 0 and current_page < self.max_pages:
                    time.sleep(self.delay)

                current_page += 1

            except Exception as e:
                print(f"Error on page {current_page}: {e}")
                break

        return all_books
