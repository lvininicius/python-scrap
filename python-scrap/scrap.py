import sys,os
sys.path.append(os.path.dirname(__file__))
sys.path.append("./venv/lib/python3.11/site-packages/scrapy/templates/project/module")
sys.path.append("items.py")
from scrapy import Spider
from items import MovieItem, MovieItemLoader

class AdoroCinemaSpider(Spider):
    name = 'adorocinema'
    start_urls = ['https://www.adorocinema.com/filmes/melhores/']

    def parse(self, response):
        movies = response.xpath("//div[contains(@class,'card-list')]")
        for movie in movies:
            title = movie.css("a.meta-title-link::text").get()
            duration = movie.css("div.meta-body-item.meta-body-info::text").get().replace("\n", "")
            original_title = movie.xpath("div[1]//div[@class='meta-body-item']/span[2]/text()").getall()[-1]
            

            il=MovieItemLoader(item=MovieItem(), selector=movies)
            il.add_value("title",title)
            il.add_value("duration",duration)
            il.add_value("original_title",original_title)

            yield il.load_item()