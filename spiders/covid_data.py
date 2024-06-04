import scrapy
import re


def no_accent_vietnamese(s):
        s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
        s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
        s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
        s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
        s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
        s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
        s = re.sub(r'[ìíịỉĩ]', 'i', s)
        s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
        s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
        s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
        s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
        s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
        s = re.sub(r'[Đ]', 'D', s)
        s = re.sub(r'[đ]', 'd', s)
        marks_list = [u'\u0300', u'\u0301', u'\u0302', u'\u0303', u'\u0306',u'\u0309', u'\u0323']
        for mark in marks_list:
            s = s.replace(mark, '')
        return s

class CovidDataSpider(scrapy.Spider):
    name = "covid_data"
    allowed_domains = ["web.archive.org"]
    start_urls = ["https://web.archive.org/web/20210907023426/https://ncov.moh.gov.vn/vi/web/guest/dong-thoi-gian"]

    
    def parse(self, response):
        datas = response.css(".timeline-detail")
        for i in datas:
            time = i.css(".timeline-head h3::text").get()
            cases = i.css(".timeline-content p:nth-child(2)::text").get()
            casenumber = re.sub(r'\D',"", cases)
            case_detail = i.css(".timeline-content p:nth-child(3)::text").get()
            case_detail_final = no_accent_vietnamese(case_detail)
            city_name_list = []
            a = re.findall(r"\b([A-Za-z\s]+)\s*\(",  case_detail_final)
            c = [match.strip() for match in a]
            b = ["An Giang","Ho Chi Minh", "Ba Ria - Vung Tau", "Bac Giang", "Bac Kan", "Bac Lieu", "Bac Ninh", "Ben Tre", "Binh Dinh", "Binh Duong", "Binh Phuoc", "Binh Thuan", "Ca Mau", "Can Tho", "Cao Bang", "Da Nang", "Dak Lak", "Dak Nong", "Dien Bien", "Dong Nai", "Dong Thap", "Gia Lai", "Ha Giang", "Ha Nam", "Ha Noi", "Ha Tinh", "Hai Duong", "Hai Phong", "Hau Giang", "Hoa Binh", "Hung Yen", "Khanh Hoa", "Kien Giang", "Kon Tum", "Lai Chau", "Lam Dong", "Lang Son", "Lao Cai", "Long An", "Nam Dinh", "Nghe An", "Ninh Binh", "Ninh Thuan", "Phu Tho", "Phu Yen", "Quang Binh", "Quang Nam", "Quang Ngai", "Quang Ninh", "Quang Tri", "Soc Trang", "Son La", "Tay Ninh", "Thai Binh", "Thai Nguyen", "Thanh Hoa", "Thua Thien Hue", "Tien Giang", "Tra Vinh", "Tuyen Quang", "Vinh Long", "Vinh Phuc", "Yen Bai"]
            for j in c:
                if j in b:
                    city_name_list.append(j)
            
            city_case_list = re.findall(r"\((.*?)\)", case_detail_final)
            
            dict_city = { city_name_list[i]: city_case_list[i] for i in range(len(city_name_list))}
            yield{
                "time": time,
                "newcase": int(casenumber),
                "city_case": dict_city
                }
