# -*- coding:utf-8 -*-
import scrapy
import re
import os
import urllib
from scrapy.selector import Selector
from scrapy.http import HtmlResponse,Request
from voguepic.items import VoguepicItem

index = 1

class baidu_spider(scrapy.spiders.Spider):

    name = "baidupic"

    def start_requests(self):
        urls = [
            'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=前卫%20服装&pn=0&gsm=50&ct=&ic=0&lm=-1&width=0&height=0',
        ]
        for url in urls:
            yield Request(url=url,
                          meta={
                              'dont_redirect': True,
                              'handle_httpstatus_list': [302]
                          },
                          callback=self.parse)

    def parse(self, response):
        hxs = Selector(response) #创建查询对象

        piclinks = hxs.xpath('//body[@class="flip"]/div[@id="wrapper"]/div/div[@id="imgid"]').extract()
        print "total number of image-links: ",len(piclinks)
        print "image link: ", piclinks

        for i in range(len(piclinks)):
            onelink = hxs.xpath('//div[@id="imgid"]/ul/li[%d]'%i).extract_first()
            if onelink:
                true_link = onelink
                true_link = "https://image.baidu.com" + str(true_link)
                print "present image link: ", true_link
                yield Request(true_link,
                              meta={
                                  'dont_redirect': True,
                                  'handle_httpstatus_list': [302]
                              },
                              callback=self.pic_parse)

        links = hxs.xpath('//*[@id="page"]/a[10]/@href').extract_first()

        if links:
            true_link = links
            true_link = "https://image.baidu.com" + str(true_link)
            print "next page link: ", true_link
            yield Request(true_link,
                          meta={
                              'dont_redirect': True,
                              'handle_httpstatus_list': [302]
                          },
                          callback=self.parse)
        else:
            print "no more next link "

    def pic_parse(self, response):
        global index
        now_hxs = Selector(response)
        stylename = "qianwei"

        true_pic = now_hxs.xpath('//*[@id="currentImg"]/@src').extract()
        if true_pic:
            file_name = "%s%d.jpg"%(stylename, index)
            file_path = os.path.join("G:\\stylepics\\qianwei",file_name)
            true_pic = str(true_pic)
            aa,true_pic,bb = true_pic.split("\'")
            urllib.urlretrieve(true_pic,file_path)
            index = index + 1