import scrapy
from ..items import RoleItem

SELECTOR_MAP = {
    "lever": {
        "DEPARTMENTS_SELECTOR": ".postings-group",
        "DEPARTMENT_SELECTOR": '.posting-category-title::text',
        "OPENINGS_SELECTOR": ".posting",
        "TITLE_SELECTOR": "h5::text   ",
        "LOCATION_SELECTOR": '.location::text',
        "LINK_SELECTOR": ".posting-apply a::attr('href')"
    },
    "greenhouse": {
        "DEPARTMENTS_SELECTOR": "section.level-0",
        "DEPARTMENT_SELECTOR": 'h3::text',
        "OPENINGS_SELECTOR": ".opening",
        "TITLE_SELECTOR": "a::text",
        "LOCATION_SELECTOR": '.location::text',
        "LINK_SELECTOR": "a::attr('href')"
    }
}

class JobSpider(scrapy.Spider):
    name = 'jobs'

    custom_settings = {
        'FEEDS': {'role_data.json': {'format': 'json', 'overwrite': True}}
    }

    def __init__(self, start_urls, job_board_name):
        self.start_urls = start_urls
        self.job_board_name = job_board_name

    def sanitize_string(self, department):
        if department != None:
            return department.lstrip().rstrip()
        else:
             return "Other"
    
    def parse(self, response):

        for department in response.css(SELECTOR_MAP[self.job_board_name]["DEPARTMENTS_SELECTOR"]):
                for opening in department.css(SELECTOR_MAP[self.job_board_name]["OPENINGS_SELECTOR"]):
                        
                    link = opening.css(SELECTOR_MAP[self.job_board_name]['LINK_SELECTOR']).extract_first()

                    if self.job_board_name == 'greenhouse':
                         link = f"https://boards.greenhouse.io{opening.css(SELECTOR_MAP[self.job_board_name]['LINK_SELECTOR']).extract_first()}"   

                    # items["title"] = f"{opening.css(SELECTOR_MAP[self.job_board_name]['TITLE_SELECTOR']).extract_first()}"
                    # items["department"] = f"{self.sanitize_string(department.css(SELECTOR_MAP[self.job_board_name]['DEPARTMENT_SELECTOR']).extract_first())}"
                    # items["location"] = f"{opening.css(SELECTOR_MAP[self.job_board_name]['LOCATION_SELECTOR']).extract_first()}"
                    # items["link"] = link
                    item = RoleItem(
                        title = opening.css(SELECTOR_MAP[self.job_board_name]['TITLE_SELECTOR']).extract_first(),
                        department = self.sanitize_string(department.css(SELECTOR_MAP[self.job_board_name]['DEPARTMENT_SELECTOR']).extract_first()),
                        location = opening.css(SELECTOR_MAP[self.job_board_name]['LOCATION_SELECTOR']).extract_first(),
                        link = link
                    )

                    yield item

                    # yield {
                    #     'title': opening.css(SELECTOR_MAP[self.job_board_name]["TITLE_SELECTOR"]).extract_first(),
                    #     'department': self.sanitize_string(department.css(SELECTOR_MAP[self.job_board_name]["DEPARTMENT_SELECTOR"]).extract_first()),
                    #     'location': opening.css(SELECTOR_MAP[self.job_board_name]["LOCATION_SELECTOR"]).extract_first(),
                    #     'link': link
                    # }