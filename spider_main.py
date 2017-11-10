#coding:utf8
from baike_spider2 import url_maneger, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_maneger.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.addNewUrl(root_url)
        while self.urls.hasNewUrl():
            try:
                new_url = self.urls.getNewUrl()
                print('craw %d:%s'%(count,new_url))
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.addNewUrls(new_urls)
                self.outputer.collectData(new_data)
                
                if count == 1000:
                    break;
                count += 1
            except:
                print("craw failed!")
        self.outputer.outputHtml()

if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)