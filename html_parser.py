#coding:utf8
from bs4 import BeautifulSoup
import re
import urlparse
        
class HtmlParser(object):
  
    def getNewUrls(self, page_url, soup):
        links = soup.find_all('a',href = re.compile(r"/view/\d+\.htm"))
        new_urls = set()
        
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    
    def getNewData(self, page_url, soup):
        res_data = {}
        #url
        res_data['url'] = page_url
        
        #<dl class="lemmaWgt-lemmaTitle lemmaWgt-lemmaTitle-">
        #<h1>Python</h1><dd class="lemmaWgt-lemmaTitle-title">
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div',class_ = "lemma-summary")
        res_data['summary'] = summary_node.get_text()
        
        return res_data
    
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        
        new_urls = self.getNewUrls(page_url,soup)
        new_data = self.getNewData(page_url,soup)
        return new_urls,new_data