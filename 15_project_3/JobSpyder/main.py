from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import json

process = CrawlerProcess(get_project_settings())

# process.crawl("company")

with open('company_data.json') as file:
         data = json.load(file)

for company in data:
        print(company["open_roles"])

process.start()  # the script will block here until the crawling is finished