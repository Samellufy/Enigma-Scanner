import requests
import urllib.parse as urlparse
from bs4 import BeautifulSoup
import threading

# target_url = "https://0aec002c0323dba880118ff2006a00a6.web-security-academy.net/"

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

# Use a lock to prevent race conditions when updating the target_links list
lock = threading.Lock()

class Crawler:
    def __init__(self,target_url):
        self.target_links = []
        self.target_url = target_url

    def crawl(self):
        try:
            response = requests.get(self.target_url,headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                links = [a['href'] for a in soup.find_all('a', href=True)]
            else:
                print(f"Failed to retrive the page. Status Code: {response.status_code}")
                return
            with lock:
                for link in links:
                    if self.target_url in link:
                        self.target_links.append(link)
                    link = urlparse.urljoin(str(self.target_url), str(link))
                    if '#' in link and '#' not in self.target_url:
                        link = link.split('#')[0]
                        self.target_links.append(link)
                    if self.target_url in link and link not in self.target_links:
                        # print(link)
                        self.target_links.append(link)

        except Exception as e:
            print(f"Exception occured {e}")

    def start_crawling(self):

        self.crawl()
        for thread in threading.enumerate():
            if thread != threading.current_thread():
                thread.join()
        return self.target_links
#             for link in links:
#                 link = urlparse.urljoin(url, link)
#                 if '#' in link and '#' not in target_url:
#                     link = link.split('#')[0]
#                 if target_url in link and link not in target_links:
#                     print(link)
#                     target_links.append(link)
#                     # Use threading to crawl links concurrently
#                     threading.Thread(target=crawl, args=(link,)).start()
#
#     except Exception as e:
#         print(f"Error: {e}")
#
# def login_form(url):
#     pass
#
# if __name__ == "__main__":
#     crawl(target_url)
#
#     # Wait for all threads to finish
#     for thread in threading.enumerate():
#         if thread != threading.current_thread():
#             thread.join()
#
#     for link in target_links:
#         if 'my-account' in link:
#             print(link)
