import requests
import os
import time
current_directory = os.path.dirname(os.path.realpath(__file__))

class Time_based_sqli:
    def __init__(self,target_url,s):
        self.target_url = target_url
        self.s = s
        self.blind_time_sqli = 0
        self.types_of_sql_injections_possble = []
        self.successful_payload = []
        self.time_based_payloads = os.path.join(current_directory, '..', 'Payloads', 'time_based.txt')
        self.payloads = []
        self.generate_payloads()

    def generate_payloads(self):
        with open(self.time_based_payloads, 'r') as data:
            for payload in data:
                payload = payload.strip()
                self.payloads.append(payload)        

    def check_for_time_based_sqli(self):
        found_cookie = {}
        response = self.s.get(self.target_url)
        got_cookies = self.s.cookies.get_dict()
        found_cookie = got_cookies
        print(found_cookie)
        print(got_cookies)
        for payload in self.payloads:
            found_cookie['TrackingId'] = payload
            print(found_cookie)
            response = self.s.get(self.target_url, cookies=found_cookie)
            got_cookies = self.s.cookies.get_dict()
            if int(response.elapsed.total_seconds()) >= 5:
                print(f"Blind time-based SQL injection possible -> {payload}")
                self.successful_payload.append(payload)
                self.blind_time_sqli = 1
                break
    
    def get_security_report_content(self):
        content = []
        if self.blind_time_sqli == 1:
            content.append(f"Target URL: {self.target_url}")
            content.append(f"Blind Time based sql injection possible {self.target_url} -> Using payloads -> {self.successful_payload}")
            return content


