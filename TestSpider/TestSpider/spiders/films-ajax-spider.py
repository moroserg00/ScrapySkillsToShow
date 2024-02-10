import scrapy
import json


class FilmsSpider(scrapy.Spider):
    name = "films"

    allowed_domains = ["https://www.scrapethissite.com/pages/ajax-javascript/"]

    # start_urls задает список веб-страниц с которых начинается парсинг
    # я нашел их опытным путем, изучая инструменты разработчика
    start_urls = ["https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2010",
                  "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2011",
                  "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2012",
                  "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2013",
                  "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2014",
                  "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2015"]

    def parse(self, response):
        # так как content-type у нас json, то нужно использовать метод json.loads()
        data = json.loads(response.text)

        # создаем список фильмов
        films_list = []
        for film_data in data:
            film_dict = film_data

            # удаляем лишний ключ year в каждом из данных о фильме, потому что нужно спарсить данные по годам
            year = film_dict["year"]
            del film_dict["year"]
            films_list.append(film_dict)

        # Возвращаем список фильмов как значение ключа year
        yield {
            str(year): films_list
        }

