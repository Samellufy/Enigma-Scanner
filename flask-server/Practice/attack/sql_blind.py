import requests 
import os
current_directory = os.path.dirname(os.path.realpath(__file__))

class Blind_conditional_sqli:
    def __init__(self,target_url,s):
        self.target_url = target_url
        self.s = s
        self.error_based_blind_sqli = 0
        self.response = s.get(self.target_url)
        self.response = s.get(self.target_url)
        self.detection_source = os.path.join(current_directory, '..', 'Payloads', 'detection_source.txt')
        self.got_cookies = {}

    def get_cookie(self):
        got_cookies = self.s.cookies.get_dict()
        self.got_cookies = got_cookies      
    
        

    def check_for_blind_conditional_sqli(self):
            self.get_cookie()
            for cookie_to_be_changed in self.got_cookies:
                if cookie_to_be_changed in self.got_cookies:
                    for cokie in self.got_cookies:
                        if cookie_to_be_changed==cokie:
                            self.got_cookies[cookie_to_be_changed] = self.got_cookies[cookie_to_be_changed]+"'"
                            updated_cookie = self.got_cookies
                            print(updated_cookie)
                response2 = self.s.get(self.target_url,cookies=updated_cookie)
                with open(self.detection_source,'r') as errors:
                    for error in errors:
                        error = error.strip()
                        if error in response2.text:
                            print("Blind error baed sql injection possibility")
                            self.error_based_blind_sqli = 1
                            break
    def get_security_report_content(self):
        content = []
        if self.error_based_blind_sqli == 1:
            if self.error_based_blind_sqli == 1:
                content.append(f"Target URL: {self.target_url}")
                content.append(f"Blind error based injection possible {self.target_url}")
                return content
        




