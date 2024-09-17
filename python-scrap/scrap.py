import scrapy

class AdoroCinemaSpider(scrapy.Spider):
    name = 'adorocinema'
    start_urls = ['https://www.adorocinema.com/filmes/melhores/']

    def parse(self, response):
        movies = response.xpath("//div[contains(@class,'card-list')]")
        for movie in movies:
            yield {
                "title": movie.css("a.meta-title-link::text").get(),
                "duration": movie.css("div.meta-body-item.meta-body-info::text").get(default='').replace(" ", ""),
                "original_title": movie.xpath("div[1]//div[@class='meta-body-item']/span[2]/text()").get(),
            }
