import scrapy

class TerabyteShopSpider(scrapy.Spider):
    name = 'terabyteshop_spider'
    start_urls = ['https://www.terabyteshop.com.br/busca?str=RTX+4060']

    custom_settings = {
        'DOWNLOAD_DELAY': 10,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'LOG_LEVEL': 'DEBUG',
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
        },
        'HTTP_PROXY': 'http://192.168.1.104:8080',  # Defina seu proxy aqui
        'RETRY_ENABLED': True,
        'RETRY_TIMES': 5,
        'RETRY_HTTP_CODES': [403, 500, 502, 503, 504],
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for product in response.css('div.product-item'):
            product_name = product.css('.prod-name::text').get().strip()
            yield {'nome_placa': product_name}
