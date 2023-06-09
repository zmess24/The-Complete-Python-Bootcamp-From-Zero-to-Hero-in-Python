# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyItem(scrapy.Item):
    name = scrapy.Field()
    company_link = scrapy.Field()
    logo = scrapy.Field()
    industries = scrapy.Field()
    job_board = scrapy.Field()
    open_roles = scrapy.Field()

class RoleItem(scrapy.Item):
    title = scrapy.Field()
    location = scrapy.Field()
    link = scrapy.Field()
    department = scrapy.Field()