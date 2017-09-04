# Scrapy_Pics_From_Baidu

针对传统网页与瀑布流网页，进行不同方式的图片爬取。

针对传统网页版进行爬取时，使用xpath无法获取//div[@id="imgid"]/ul/li下的内容，分析原因可能网页是用js动态加载的。
针对瀑布流版进行爬取时，是直接从包含图片url的json文件中获取。

以上两种方式都是通过urllib.urlretrieve(true_pic,file_path)方式保存图片；
通过pipeline保存图片的方式如下。

爬虫主文件：
item['IMG_URL'] = [img['middleURL']]
yield item

setting文件：
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1
}
IMAGES_URLS_FIELD = 'IMG_URL'
IMAGES_STORE = 'G:\\stylepics'
