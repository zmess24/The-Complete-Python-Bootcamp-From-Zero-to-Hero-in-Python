import scrapy
from scrapy.crawler import CrawlerProcess
from spiders import TopStartupsSpider

process = CrawlerProcess(
    settings={
        "FEEDS": {
            "company_data.json": {"format": "json", "overwrite": True},
        },
    }
)
process.crawl(TopStartupsSpider)
process.start()  # the script will block here until the crawling is finished

