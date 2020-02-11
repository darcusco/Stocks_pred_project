import scrapy

class NewsSpider (scrapy.Spider):
    name = 'spacex'

    start_urls=['https://www.teslarati.com/category/spacex/']

    def parse(self, response):
        for article_link in response.xpath("//li[@class='infinite-post']/a/@href").getall():
            
            yield scrapy.Request(article_link,callback=self.parse_post)
        
        for i in range(48):
            href="https://www.teslarati.com/category/spacex/page/"+ str(i+2)+"/"
            yield scrapy.Request(href,callback=self.parse)
        # pagenum = response.xpath("//div[@class='pagination']/span/text()")
        # pagenum =pagenum[-2:]

        # i=0
        # for paginame in response.xpath("//div[@class='pagination']/a/text()"):
        #     print(i)
        #     if paginame == ("Next ›"):
        #         print('ses')
        #         next_page = response.xpath("//div[@class='pagination']/a/@href").getall()[i]
        #         yield scrapy.Request(next_page,callback=self.parse)
        #     i+=1
        
            
    def parse_post(self, response):
        def fetch_data(x_path):
            return response.xpath(x_path).getall()
        yield{
            'date':fetch_data("//time[@class='post-date updated']/text()")[0],
            'headline':fetch_data("//h1/text()")[0],
            'tag':fetch_data("//span[@class='feat-cat']/text()")[0],
            'author':fetch_data("//span[@class='author-name vcard fn author']/a/text()")[0],
            'text':fetch_data("//div[@id='pico']/p//text()"),          
        }    