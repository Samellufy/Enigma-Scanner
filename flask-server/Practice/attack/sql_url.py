import requests
# from scrapping.Login import Login_form
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class Usql:
    def __init__(self,crawl_links,target_url):
        self.crawl_links = crawl_links
        self.target_url = target_url
        self.url_vulnerable_links = []
        self.payloads = os.path.join(current_dir,'..','Payloads','error_based.txt')
        # self.login_check = ['login','my-account','signin']

    def url_sqli(self):
        for link in self.crawl_links:
            with open(self.payloads,'r') as payloads:
                for payload in payloads:
                    payload = payload.strip()
                    print(link+payload)
                    response = requests.get(link + payload)
                    if 'server error' in (response.text).lower():
                        print(f"Url based sql inject possible on {link}")
                        self.url_vulnerable_links.append(link+payload)
                        return

                        
            
    def get_security_report_content(self):
        content = []
        if self.url_vulnerable_links:
            for link in self.url_vulnerable_links:
                content.append(f"{link} <- URL based sql injection possible")
            print(content)
            return content

    


