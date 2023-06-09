import scrapy

class JobSpider(scrapy.Spider):
    name = 'jobs'
    
    def __init__(self, start_urls, job_board):
        self.start_urls = start_urls
        self.job_board = job_board

    def sanitize_string(self, string):
        return string.lstrip().rstrip()
    
    def parse(self, response):
        DEPARTMENTS_SELECTOR  = ".postings-group"
        DEPARTMENT_SELECTOR = '.posting-category-title::text'
        OPENINGS_SELECTOR = ".posting"
        TITLE_SELECTOR = "h5::text   "
        LOCATION_SELECTOR = '.location::text'
        LINK_SELECTOR = ".posting-apply a::attr('href')"

        for department in response.css(DEPARTMENTS_SELECTOR):
                for opening in department.css(OPENINGS_SELECTOR):
                    yield {
                        'title': opening.css(TITLE_SELECTOR).extract_first(),
                        'department': self.sanitize_string(department.css(DEPARTMENT_SELECTOR).extract_first()),
                        'location': opening.css(LOCATION_SELECTOR).extract_first(),
                        'link': opening.css(LINK_SELECTOR).extract_first()
                    }