from Practice.Crawler import Crawler
from Practice.Scrapping import Scrapping
import urllib.parse as urlparse
import requests

class Links:
    def __init__(self,target_url,crawl_links):
        self.target_url = target_url
        self.crawl_links = crawl_links

    # def get_links(self):
    #     crawler = Crawler(self.target_url)
    #     print(crawler.start_crawling())
    #     return crawler.start_crawling()

    def img_links(self):
        img_links = []
        for link in self.crawl_links:
            print(link)
            scrap = Scrapping(link)
            if scrap.get_img_link():
                img_links.append(scrap.get_img_link())
        return img_links








