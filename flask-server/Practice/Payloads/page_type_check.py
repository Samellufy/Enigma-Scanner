import requests


class PageCheck:

    def __init__(self,crawl_links):
        self.crawl_links = crawl_links
        self.payloads = ['login','my-account','signin']

    def is_login_page(self):
        for link in self.crawl_links:
            for payload in self.payloads:
                if payload in link.lower():
                    return link

