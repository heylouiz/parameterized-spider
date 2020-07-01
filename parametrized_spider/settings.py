BOT_NAME = 'parametrized_spider'

SPIDER_MODULES = ['parametrized_spider.spiders']
NEWSPIDER_MODULE = 'parametrized_spider.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    'scrapy.extensions.corestats.CoreStats': None,
    'parametrized_spider.extensions.CustomCoreStats': 1,
}
