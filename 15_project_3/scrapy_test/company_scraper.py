import scrapy
from scrapy.crawler import CrawlerProcess
from spiders import TopStartupsSpider

settings={
    "FEEDS": { "company_data.json": {"format": "json", "overwrite": True } },
}
process = CrawlerProcess(settings)
process.crawl(TopStartupsSpider)
process.start()  # the script will block here until the crawling is finished

