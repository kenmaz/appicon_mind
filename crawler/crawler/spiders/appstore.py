import scrapy
from crawler.items import CrawlerItem

class AppStoreSpider(scrapy.Spider):
    name = "appstore"
    start_urls = ["https://itunes.apple.com/jp/genre/ios/id36?mt=8"]
    genre_name = ''
    app_name = ''

    def parse(self, response):
        for a in response.css('a.top-level-genre'):
            self.genre_name = a.css('::text').extract_first()
            yield response.follow(a, callback=self.parse_genre)

    def parse_genre(self, response):
        for a in response.css('#selectedcontent li a'):
            self.app_name = a.css('::text').extract_first()
            yield response.follow(a, callback=self.parse_app)

    def parse_app(self, response):
        icon_url = response.css('#main #content div.application.product.lockup .artwork img::attr(src-swap)').extract_first()
        descriptions = [x.extract() for x in response.css('.product-review p::text')]
        item = CrawlerItem()
        item['image_urls'] = [icon_url]
        item['app_name'] = self.app_name
        item['genre_name'] = self.genre_name
        item['descriptions'] = descriptions
        return item
