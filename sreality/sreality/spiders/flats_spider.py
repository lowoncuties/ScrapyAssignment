import scrapy
import json
from sreality.items import FlatItem

class QuotesSpider(scrapy.Spider):
    name = "flats"
    start_urls = ['https://www.sreality.cz/hledani/prodej/byty']

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.sreality.cz/hledani/prodej/byty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84",

    }

    def parse(self, response):
        url = 'https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500&tms=1667054002378'

        request = scrapy.Request(url, callback=self.parse_api, headers=self.headers)

        yield request

    def parse_api(self, response):
        flat_item = FlatItem()
        raw_data = response.body
        data = json.loads(raw_data)
        img_url = ""
        for flat in data['_embedded']['estates']:
            for img in flat['_links']['image_middle2']:
                img_url = img['href']
            
            
            flat_item["title"] = flat['name']
            flat_item["img"]= img_url
            yield flat_item