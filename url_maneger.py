#coding:utf8
class UrlManager(object):
    def __init__(self):
        self.newUrls = set()   #未爬取的url集合
        self.oldUrls = set()    #已经爬取的url集合
        
    def hasNewUrl(self):
        return len(self.newUrls)!=0

    def getNewUrl(self):
        new_url = self.newUrls.pop()
        self.oldUrls.add(new_url)
        return new_url
        
    def addNewUrl(self,url):
        if url is None:
            return
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url)
        
    def addNewUrls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.addNewUrl(url)
