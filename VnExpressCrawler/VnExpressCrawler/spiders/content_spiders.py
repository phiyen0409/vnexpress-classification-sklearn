import scrapy
import csv
import pandas as pd

from ..items import VnexpressContentItem


class QuoteSpider(scrapy.Spider):
    name = 'vnexpresscontent'
    start_urls = []

    datalink=pd.read_csv('./link.csv')


    for j in range(0,len(datalink)//10000):
        n=10000*j
        if (n>len(datalink)):
            if (len(datalink)>(n-10000)):
                for i in range(n-10000,len(datalink)):
                    start_urls.append(str(datalink.values[i,0]))
            else:
                break
        else:
            for i in range(n-10000,n):
                start_urls.append(str(datalink.values[i,0]))


    # def parse(self, response):
    #     items = VnexpressContentItem()
    #     sidebar = response.css('.sidebar_1')
    #
    #     title = sidebar.css('.title_news_detail::text').extract()
    #     label = response.css('ul.breadcrumb')[0].css('a::text')[0].extract()
    #
    #     items['title'] = title
    #     items['label'] = label
    #     yield items

    # for i in range(0,500):
    #     start_urls.append(str(datalink.values[i,0]))


    def parse(self, response):
        items = VnexpressContentItem()
        sidebar = response.css('.sidebar_1')
        title = sidebar.css('.title_news_detail::text').extract()
        content = sidebar.css('p.Normal::text').extract()
        # news = str(title) + " " + str(content)
        label = response.css('ul.breadcrumb')[0].css('a::text')[0].extract()

        items['title']=title
        items['content'] = content
        items['label'] = label
        yield items
