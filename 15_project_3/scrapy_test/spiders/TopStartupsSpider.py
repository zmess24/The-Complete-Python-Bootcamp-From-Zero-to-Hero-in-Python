import scrapy
from scrapy.crawler import CrawlerProcess

class TopStartupsSpider(scrapy.Spider):
    name = 'topstartupsspider'
    start_urls = ['https://topstartups.io/?industries=Artificial+Intelligence&industries=Analytics&industries=Biotech&industries=Collaboration&industries=Consumer&industries=Crypto&industries=Cybersecurity&industries=Data+Science&industries=E-Commerce&industries=EdTech&industries=Enterprise+Software&industries=FinTech&industries=Gaming&industries=Hardware&industries=Healthcare&industries=Marketplace&industries=Media&industries=Retail&industries=SaaS&industries=Sales&industries=Space&industries=Sustainability']

    def sanitize_url(self, url):
        if url == None:
            return ""
        elif "?" in url:
            return url.split('?')[0]
        else:
            return url

    def parse(self, response):
        COMPANY_SELCTOR  = "#item-card-filter"
        NAME_SELECTOR = "h3::text"
        COMPANY_LINK_SELCTOR = "#startup-website-link::attr('href')"
        JOB_LINK_SELECTOR = "#view-jobs::attr('href')"
        LOGO_SELECTOR = "img::attr('src')"
        NEXT_LINK = ".infinite-more-link"
        INDUSTRY_SELECTOR = "#industry-tags::text"


        for company in response.css(COMPANY_SELCTOR):
            if company.css(NAME_SELECTOR).extract_first() != None and company.css(COMPANY_LINK_SELCTOR).extract_first() != None:

                yield {
                    'name': company.css(NAME_SELECTOR).extract_first(),
                    'company_link': self.sanitize_url(company.css(COMPANY_LINK_SELCTOR).extract_first()),
                    'job_board': self.sanitize_url(company.css(JOB_LINK_SELECTOR).extract_first()),
                    'logo': company.css(LOGO_SELECTOR).extract_first(),
                    'industries': company.css(INDUSTRY_SELECTOR).extract()
                }

        for next_page in response.css(NEXT_LINK):
            yield response.follow(next_page, self.parse)

process = CrawlerProcess(
    settings={
        "FEEDS": {
            "company_data.json": {"format": "json", "overwrite": True },
        },
    }
)
process.crawl(TopStartupsSpider)
process.start() 