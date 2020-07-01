"""
Extension for collecting core stats like items scraped and start/finish times
"""
from datetime import datetime

from scrapy.extensions.corestats import CoreStats


class CustomCoreStats(CoreStats):

    def spider_closed(self, spider, reason):
        finish_time = datetime.utcnow()
        elapsed_time = finish_time - self.start_time
        elapsed_time_seconds = elapsed_time.total_seconds()
        self.stats.set_value('elapsed_time_seconds', elapsed_time_seconds, spider=spider)
        self.stats.set_value('finish_time', finish_time, spider=spider)
        self.stats.set_value('finish_reason', spider.finish_reason, spider=spider)
        self.stats.set_value('item_scraped_count', spider.item_scraped_count, spider=spider)
        self.stats.set_value('downloader/request_count', spider.request_count, spider=spider)
        if spider.error_count:
            self.stats.set_value('log_count/ERROR', spider.error_count, spider=spider)
        if spider.crawlera_banned:
            self.stats.set_value('crawlera/response/banned', spider.crawlera_banned, spider=spider)
            self.stats.set_value('crawlera/response/error', spider.crawlera_banned, spider=spider)
            self.stats.set_value('crawlera/response/error/banned', spider.crawlera_banned, spider=spider)
