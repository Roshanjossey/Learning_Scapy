import scrapy

class FlipSpider(scrapy.Spider):
    name = "flip"
    allowed_domains = ["flipkart.com"]
    start_urls = ["http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?sid=mgl&filterNone=true&start=1&ajax=true&_=1434544629317"]
    def parse(self, response):
        for result in response.xpath('//div[@class="product-unit unit-3 browse-product new-design  quickview-required"]'):
            title = result.xpath('div[@class="pu-details lastUnit"]/div[@class="pu-title fk-font-13"]/a/@title').extract()
            link = result.xpath('div[@class="pu-details lastUnit"]/div[@class="pu-title fk-font-13"]/a/@href').extract()
            price = result.xpath('div[@class="pu-details lastUnit"]/div[@class="pu-price"]/div/div/span/text()').extract()
            print("{0} {1}".format(title[0].ljust(73), price[0].ljust(15)))
            print(link[0])
            print('\n')
        for result in response.xpath('//div[@class="product-unit unit-3 browse-product new-design  quickview-required vs-widget-required"]'):
            title = result.xpath('div[@class="pu-details lastUnit"]/div[@class="pu-title fk-font-13"]/a/@title').extract()
            link = result.xpath('div[@class="pu-details lastUnit"]/div[@class="pu-title fk-font-13"]/a/@href').extract()
            price = result.xpath('div[@class="pu-details lastUnit"]/div[@class="pu-price"]/div/div/span/text()').extract()
            print("{0} {1}".format(title[0].ljust(73), price[0].ljust(15)))
            print(link[0])
            print('\n')