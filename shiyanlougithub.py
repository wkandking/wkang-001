# -*- coding: utf-8 -*-
import scrapy
from wkang.items import WkangItem

class ShiyanlougithubSpider(scrapy.Spider):
    name = "shiyanlougithub"
    # start_url=["https://github.com/shiyanlou?page=1&tab=repositories"]
    @property
    def start_urls(self):
        urls="https://github.com/shiyanlou?page={}&tab=repositories"
        return (urls.format(i) for i in range(1,5))

    def parse(self, response):
        node_list=response.xpath("//li[@itemtype='http://schema.org/Code']")
        for node in node_list:
            item = WkangItem()
            item['name']=node.xpath("./div[1]/h3/a/text()").extract()[0].strip()
            item['update_time']=node.xpath("./div[3]/relative-time/@datetime").extract()[0]
            yield item



