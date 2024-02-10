import scrapy


class LoginSpider(scrapy.Spider):
    name = "hockey"
    start_urls = ["https://www.scrapethissite.com/pages/forms/"]

    def parse(self, response):
        # Автоматически заполняем форму текстом New York
        return scrapy.FormRequest.from_response(
            response,
            formdata={"q": "New York"},
            callback=self.after_form_request,
        )

    def after_form_request(self, response):
        # Ходим по всем ссылкам пагинации
        pagination_links = response.xpath("//ul[contains(@class, 'pagination')]/li/a/@href")
        yield from response.follow_all(pagination_links, self.after_form_request)

        # Если в ссылке нет параметра page_num, то игнорируем ее
        if 'page_num' in response.url:
            # Собираем данные о командах
            teams = response.xpath("//tr[contains(@class, 'team')]")

            for team in teams:

                yield {
                    "Team Name": team.xpath("td[contains(@class, 'name')]/text()").get().strip(),
                    "Year": team.xpath("td[contains(@class, 'year')]/text()").get().strip(),
                    "Wins": team.xpath("td[contains(@class, 'wins')]/text()").get().strip(),
                    "Losses": team.xpath("td[contains(@class, 'losses')]/text()").get().strip(),
                    "OT Losses": team.xpath("td[contains(@class, 'ot-losses')]/text()").get().strip(),
                    "Win %": team.xpath("td[contains(@class, 'pct')]/text()").get().strip(),
                    "Goals For (GF)": team.xpath("td[contains(@class, 'gf')]/text()").get().strip(),
                    "Goals Against (GA)": team.xpath("td[contains(@class, 'ga')]/text()").get().strip(),
                    "+ / -": team.xpath("td[contains(@class, 'diff')]/text()").get().strip()
                }
