from urllib.parse import urljoin

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import (PEP_SPIDER_NAME,
                                PEP_ALLOWED_DOMAINS,
                                PEP_START_URLS)


class PepSpider(scrapy.Spider):
    name = PEP_SPIDER_NAME
    allowed_domains = PEP_ALLOWED_DOMAINS
    start_urls = PEP_START_URLS

    def parse(self, response):
        numerical = response.xpath('//*[@id="numerical-index"]')
        tab_body = numerical.css('tbody')
        tab_rows = tab_body.css('tr').getall()
        for tab_row in tab_rows:
            row = scrapy.Selector(text=tab_row)
            link = row.css('a::attr(href)').get()
            pep_link = urljoin(self.start_urls[0], f'{link}/')
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number = response.xpath(
            '//*[@id="pep-page-section"]/header/ul/li[3]').re(r'\d+')[0]
        name = response.css('h1.page-title::text').get()
        status = response.xpath(
            'string(//dt[contains(text(), "Status")]/following-sibling::dd[1])'
        ).get()
        data = {
            'number': number,
            'name': name,
            'status': status,
        }
        yield PepParseItem(data)
