# -*- coding:utf-8 -*-
import scrapy
import re
import os
import urllib
import json
from scrapy.selector import Selector
from scrapy.http import HtmlResponse,Request
from voguepic.items import VoguepicItem

index = 1

class baidu2_spider(scrapy.spiders.Spider):
    name = 'baidupic_qianwei'
    start_urls = [
        'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=前卫+服装&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=前卫+服装&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn=%d' %i for i in range(0,901,30)
    ]

    def parse(self, response):
        global index
        stylename = "qianwei"
        imgs = json.loads(response.body)['data']
        for img in imgs:
            try:
                true_pic = [img['middleURL']]
                if true_pic:
                    file_name = "%s%d.jpg" % (stylename, index)
                    file_path = os.path.join("G:\\stylepics\\qianwei", file_name)
                    true_pic = str(true_pic)
                    aa, true_pic, bb = true_pic.split("\'")
                    urllib.urlretrieve(true_pic, file_path)
                    index = index + 1
            except Exception as e:
                print e