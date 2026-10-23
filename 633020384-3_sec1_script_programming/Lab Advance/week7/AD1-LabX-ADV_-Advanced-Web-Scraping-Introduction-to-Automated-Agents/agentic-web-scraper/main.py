import sys
import os
import json

# ตั้งค่า Path ค้นหาโฟลเดอร์ src ให้ถูกต้อง
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from config_parser import ConfigParser
from scraper_agent import ScraperAgent

def main():
    # 1. โหลดข้อมูลการตั้งค่าผ่านไฟล์ config_parser.py
    config_path = os.path.join(os.path.dirname(__file__), 'configs', 'example_site_config.json')
    parser = ConfigParser(config_path)
    config = parser.load_config()

    # 2. เริ่มต้นการทำงานของบอทดึงข้อมูลสินค้า
    agent = ScraperAgent(config)
    books_data = agent.scrape_books()

    # 3. จัดการสร้างโฟลเดอร์และเซฟข้อมูลออกเป็นไฟล์ JSON
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    output_file = os.path.join(data_dir, 'scraped_products.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(books_data, f, indent=4, ensure_ascii=False)

    # 📌 ข้อความพิมพ์สรุปเมื่อจบงานให้เหมือนภาพตัวอย่าง
    print(f"Successfully scraped {len(books_data)} items and saved to data\\scraped_products.json")

if __name__ == "__main__":
    main()
