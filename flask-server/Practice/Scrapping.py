import requests
from bs4 import BeautifulSoup
import sys


class Scrapping:

    def __init__(self,target_url):
        self.target_url = target_url
        self.response = requests.get(self.target_url)

    def get_img_link(self):
        if self.response.status_code == 200:
            soup = BeautifulSoup(self.response.text, 'html.parser')
            links = [img['src'] for img in soup.find_all('img', src=True) if '=' in img['src']]
            for link in links:
                return link

