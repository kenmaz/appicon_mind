import scrapy
from crawler.items import CrawlerItem

class AppStoreSpider(scrapy.Spider):
    name = "appstore"
    start_urls = ["https://itunes.apple.com/jp/genre/ios/id36?mt=8"]

    def parse(self, response):
        for a in response.css('a.top-level-genre'):
            yield response.follow(a, callback=self.parse_genre)

    def parse_genre(self, response):
        for a in response.css('#selectedcontent li a'):
            yield response.follow(a, callback=self.parse_app)

    def parse_app(self, response):
        icon_url = response.css('#main #content div.application.product.lockup .artwork img::attr(src-swap)').extract_first()
        descriptions = [x.extract() for x in response.css('.product-review p::text')]
        app_name = response.css('#title h1::text').extract_first()
        genre_name = response.css('li.genre a span::text').extract_first()
        item = CrawlerItem()
        item['image_urls'] = [icon_url]
        item['app_name'] = app_name
        item['app_url'] = response.url
        item['genre_name'] = genre_name
        item['descriptions'] = descriptions
        return item
