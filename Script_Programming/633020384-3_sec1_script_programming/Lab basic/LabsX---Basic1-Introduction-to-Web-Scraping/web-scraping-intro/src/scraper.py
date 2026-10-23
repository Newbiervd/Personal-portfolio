import requests
from bs4 import BeautifulSoup

class SimpleWebScraper:
    def __init__(self, url):
        self.url = url

    def scrape_main_titles(self):
        """
        ดึงข้อมูลชื่อหนังสือและรายชื่อบทเรียนจากเว็บเป้าหมาย
        """
        try:
            # พิมพ์ข้อความสถานะตามรูปแบบผลลัพธ์ที่คุณต้องการ
            print(f"กำลังดาวน์โหลดเนื้อหาจาก: {self.url}")
            
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(self.url, headers=headers)
            response.raise_for_status()
            
            print("ดาวน์โหลดเนื้อหาสำเร็จ")

            soup = BeautifulSoup(response.text, 'html.parser')

            # หาชื่อหนังสือจากแท็ก <h1> แรก
            book_title = "3rd Edition"
            h1_tag = soup.find('h1')
            if h1_tag:
                book_title = h1_tag.get_text(strip=True)

            # กรองและเก็บรายชื่อบทเรียนทั้งหมดจากแท็ก <li>
            chapter_titles = []
            for li in soup.find_all('li'):
                text = li.get_text(strip=True)
                
                # กรองเอาเฉพาะรายการบทเรียนหลัก
                if (text.startswith("Introduction") or 
                    text.startswith("Chapter") or 
                    text.startswith("Appendix")):
                    
                    if text not in chapter_titles:
                        chapter_titles.append(text)

            return {
                'book_title': book_title,
                'chapter_titles': chapter_titles
            }

        except Exception as e:
            print(f"เกิดข้อผิดพลาด: {e}")
            return None
