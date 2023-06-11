# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass

@dataclass
class CompanyItem():
    name: str
    company_link: str
    logo: str
    industries: str
    job_board: str
    open_roles: list

@dataclass
class RoleItem():
    title: str
    location: str
    department: str
    link: str