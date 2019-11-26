import scrapy
from WebCrawl.items import WebcrawlItem


class Hongxiuwangzhan(scrapy.Spider):
    name = 'niuke'
    allowed_domain = ['www.nowcoder.com']
    start_urls = ['https://www.nowcoder.com/ta/review-java/review?page=1']

    def parse(self, response):
        question = response.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/text()').extract()
        answer = response.xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/text()').extract()
        item = WebcrawlItem()
        item['question'] = question
        item['answer'] = answer
        yield item
        pass

        for i in range(2, 120):
            next_page = 'https://www.nowcoder.com/ta/review-java/review?page='+str(i)
            yield scrapy.Request(next_page, callback=self.parse, method="Get")