import scrapy
from ..items import CompanyItem

class CompanySpider(scrapy.Spider):
    name = 'company'
    start_urls = ['https://topstartups.io/?industries=Artificial+Intelligence&industries=Analytics&industries=Biotech&industries=Collaboration&industries=Consumer&industries=Crypto&industries=Cybersecurity&industries=Data+Science&industries=E-Commerce&industries=EdTech&industries=Enterprise+Software&industries=FinTech&industries=Gaming&industries=Hardware&industries=Healthcare&industries=Marketplace&industries=Media&industries=Retail&industries=SaaS&industries=Sales&industries=Space&industries=Sustainability']

    # To store in CSV format
    custom_settings = {
        'FEEDS': {'company_data.json': {'format': 'json', 'overwrite': True}}
    }

    def sanitize_url(self, url):
        if url == None:
            return ""
        elif "?" in url:
            return url.split('?')[0]
        else:
            return url

    def parse(self, response):
        items = CompanyItem()

        COMPANY_SELCTOR  = "#item-card-filter"
        NAME_SELECTOR = "h3::text"
        COMPANY_LINK_SELCTOR = "#startup-website-link::attr('href')"
        JOB_LINK_SELECTOR = "#view-jobs::attr('href')"
        LOGO_SELECTOR = "img::attr('src')"
        NEXT_LINK = ".infinite-more-link"
        INDUSTRY_SELECTOR = "#industry-tags::text"

        for company in response.css(COMPANY_SELCTOR):
            if company.css(NAME_SELECTOR).extract_first() != None and company.css(COMPANY_LINK_SELCTOR).extract_first() != None:

                items['name'] = company.css(NAME_SELECTOR).extract_first()
                items['company_link'] = self.sanitize_url(company.css(COMPANY_LINK_SELCTOR).extract_first())
                items['job_board'] = self.sanitize_url(company.css(JOB_LINK_SELECTOR).extract_first())
                items['logo'] = company.css(LOGO_SELECTOR).extract_first()
                items['industries'] = company.css(INDUSTRY_SELECTOR).extract()

                yield items

        for next_page in response.css(NEXT_LINK):
            yield response.follow(next_page, self.parse)