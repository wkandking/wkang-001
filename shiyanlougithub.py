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
        head_url = "https://github.com"
        node_list=response.xpath("//li[@itemtype='http://schema.org/Code']")
        for node in node_list:
            item = WkangItem()
            item['name']=node.xpath("./div[1]/h3/a/text()").extract()[0].strip()
            item['update_time']=node.xpath("./div[3]/relative-time/@datetime").extract()[0]
            link=node.xpath("./div[1]/h3/a/@href").extract()[0].strip()
            url=head_url+link
            requset=scrapy.Request(url,callback=self.parse_page_data)
            requset.meta['item']=item
            yield requset
    def parse_page_data(self,reponse):
        item=reponse.meta['item']
        data_list=reponse.xpath("//span[@class='num text-emphasized']/text()").extract()
        item['commits']=int(data_list[0].strip())
        item['branches']=int(data_list[1].strip())
        item[' releases']=int(data_list[2].strip())
        yield item





