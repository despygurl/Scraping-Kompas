import scrapy

class PostsSpider(scrapy.Spider):
    name = "kompas"
    allowed_urls = ['https://www.kompas.com']
    start_urls = [
        'https://indeks.kompas.com'

    ]

    def parse(self, response):
        for post in response.css('.article__list.clearfix'):
            yield {
                'judul berita': post.css('.article__link::text').get(),
                'link berita': post.css('a ::attr(href)').get(),
                'topik berita': post.css('.article__subtitle.article__subtitle--inline::text').get(),
                'waktu': post.css('.article__date::text').get()
            }

            next_page = response.css('.paging__wrap.clearfix ::attr(href)')[-2].get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)