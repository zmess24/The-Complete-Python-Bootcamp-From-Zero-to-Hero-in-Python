from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import json

process = CrawlerProcess(get_project_settings())

# 'followall' is the name of one of the spiders of the project.
# process.crawl("company")
with open('company_data.json') as file:
         data = json.load(file)

start_urls = [company['job_board'] for company in data if 'lever' in company['job_board']]

print(start_urls)
# process.crawl('jobs', job_board="greenhouse", start_urls=start_urls)
process.start()  # the script will block here until the crawling is finished