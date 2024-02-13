from crawler import Crawler

class Data:
    def __init__(self):
        self.craw_links = []
        
        self.get_crawl_links()

    def get_crawl_links(self):
        crawl = Crawler("https://mangakakalot.com")
        self.craw_links = crawl.start_crawling()
        return self.craw_links