import scrapy


class ParameterizedSpider(scrapy.Spider):
    name = 'parameterized'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/']

    # Defaults to non error values
    item_scraped_count = 10
    finish_reason = "finished"
    request_count = 10
    error_count = 0
    crawlera_banned = 0

    def __init__(self, *args, **kwargs):
        super(ParameterizedSpider, self).__init__(*args, **kwargs)
        # Convert attributes
        self.item_scraped_count = int(self.item_scraped_count)
        self.request_count = int(self.request_count)
        self.error_count = int(self.error_count)
        self.crawlera_banned = int(self.crawlera_banned)

    def parse(self, response):
        pass
