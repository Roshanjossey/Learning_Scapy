import scrapy

class FlipSpider(scrapy.Spider):
    name = "flip"
    allowed_domains = ["flipkart.com"]
    start_urls = ["http://www.flipcart.com/mobiles/pr?sid=tyy,4io&otracker=ch_vn_mobile_filter_Top%20Brands_All/"]
    def parse(self, response):
        f = file('Phone_Details.txt', 'w')
        for result in response.xpath('//div[@class="product-unit unit-4 browse-product new-design "]'):
            title = result.xpath('div[@class="pu-details lastUnit"]/div[@class="pu-title fk-font-13"]/a/@title').extract()
            link = result.xpath('div[@class="pu-details lastUnit"]/div[@class="pu-title fk-font-13"]/a/@href').extract()
            price = result.xpath('div[@class="pu-details lastUnit"]/div[@class="pu-price"]/div/div/span/text()').extract()
            f.write("{0} {1}".format(title[0].ljust(73), price[0].ljust(15)))
            f.write(link[0])
            f.write('\n')
