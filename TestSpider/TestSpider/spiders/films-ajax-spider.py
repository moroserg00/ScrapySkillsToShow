import scrapy
import json


class FilmsSpider(scrapy.Spider):
    name = "films"

    allowed_domains = ["https://www.scrapethissite.com/pages/ajax-javascript/"]
    start_urls = ["https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2010",
                  "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2011",
                  "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2012",
                  "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2013",
                  "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2014",
                  "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2015"]

    def parse(self, response):
        data = json.loads(response.text)
        films_list = []
        for film_data in data:
            film_dict = film_data
            year = film_dict["year"]
            del film_dict["year"]
            films_list.append(film_dict)
        yield {
            str(year): films_list
        }

