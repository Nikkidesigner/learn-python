import scrapy


class WorldmeterSpider(scrapy.Spider):
    name = "worldmeter"
    allowed_domains = ["www.worldometers.info/"]
    start_urls = ["https://www.worldometers.info/coronavirus"]

    def parse(self, response):
        pass
