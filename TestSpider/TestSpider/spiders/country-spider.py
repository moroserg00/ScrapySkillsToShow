import scrapy


class CountrySpider(scrapy.Spider):
    name = "countries"

    start_urls = ["https://www.scrapethissite.com/pages/simple/"]

    def parse(self, response):
        # Доделать

        country_cards = response.xpath("//div[contains(@class, 'col-md-4 country')]")
        for country_card in country_cards:
            yield {
                "country_name": country_card.xpath("h3/text()[2]").get().strip(),
                "country_capital": country_card.xpath("div/span[contains(@class, 'country-capital')]/text()").get(),
                "country_population": country_card.xpath("div/span[contains(@class, 'country-population')]/text()").get(),
                "country_area": country_card.xpath("div/span[contains(@class, 'country-area')]/text()").get()
            }