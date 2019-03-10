

newScrapycContext = '''
import scrapy
from demo1.items import Demo1Item

class Demo1Spider(scrapy.Spider):
    name = "demoSpider"
    allowed_domains = ["travel.sina.com.cn"]
    start_urls = [
        "http://travel.sina.com.cn/domestic/news/2018-06-26/detail-ihencxtu2975652.shtml"
    ]

    def parse(self, response):
        try:
            for sel in response.xpath("//div[@class='wrap-inner']"):
                item = Demo1Item()
                item['title'] = sel.xpath("//h1[@id='artibodyTitle']/text()").extract()
                item['content_html'] = sel.xpath("//div[@class='article article_16']/p").extract()
                item['content_text'] = sel.xpath("//div[@class='article article_16']/p/text()").extract()
                item['date'] = sel.xpath("//span[@class='time-source']/text()").extract()
            yield item
        except:
            print('error')
'''

w = open('F:\\autoScrapy\\demo1\\demo1\\spiders\\spider.py','w')
w.write(newScrapycContext)
w.close()


f = open('F:\\autoScrapy\\demo1\\demo1\\spiders\\spider.py','r')
spiderFile = f.read()
f.close()
print("****************")
print(spiderFile)
print("****************")