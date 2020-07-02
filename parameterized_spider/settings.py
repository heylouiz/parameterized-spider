BOT_NAME = 'parameterized_spider'

SPIDER_MODULES = ['parameterized_spider.spiders']
NEWSPIDER_MODULE = 'parameterized_spider.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    'scrapy.extensions.corestats.CoreStats': None,
    'parameterized_spider.extensions.CustomCoreStats': 1,
}
