import scrapy

class FlipSpider(scrapy.Spider):
    name = "flip"
    allowed_domains = ["flipkart.com"]
    start_urls = ["http://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=ch_vn_mobile_filter_Top%20Brands_All/"]
    def parse(self, response):
        filename = response.url.split('/')[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
