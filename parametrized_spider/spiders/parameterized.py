import scrapy


class ParameterizedSpider(scrapy.Spider):
    name = 'parameterized'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/']

    def parse(self, response):
        pass
