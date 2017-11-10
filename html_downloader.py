#coding:utf8
import urllib2
        
class HtmlDownloader(object):
    
    def download(self,url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        
        if response.getcode() != 200:   #检测状态码是否为200，200代表成功
            return None
        
        return response.read()