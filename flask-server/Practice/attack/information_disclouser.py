import requests
import os
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend

import matplotlib.pyplot as plt

current_directory = os.path.dirname(os.path.realpath(__file__))

class InformationDisclouser:
    def __init__(self,target_url,crawl_links):
        self.target_url = target_url
        self.explode = [0,0,0]
        self.crawl_links = crawl_links
        self.information_disclouser_robots = []
        self.information_disclouser_link = []
        self.payload = "string"
        self.error_for_error_based = os.path.join(current_directory, '..', 'Payloads', 'information_disclouser_payload.txt')

    def check_for_robotstxt_file(self):
        check_robotstxt = requests.get(self.target_url+"robots.txt")
        if check_robotstxt.status_code == 200:
            self.information_disclouser_robots.append(self.target_url+"robots.txt")
            self.explode[0] = 0.1
            print("Found robots.txt")

    def error_based(self):
        print("checking for error based")
        for link in self.crawl_links:
            response = requests.get(link+self.payload)
            print(link)
            with open(self.error_for_error_based,'r') as errors:
                for error in errors:
                    error = error.strip()
                    if error in response.text:
                        print("checkkkkkkk")
                        print("Detected Information disclouser")
                        self.information_disclouser_link.append(link)


    def get_security_report_content(self):
        print("gettinggggg")
        content = []
        content.append(f"Target URL: {self.target_url}")
        if self.information_disclouser_link:
            for link in self.information_disclouser_link:
                content.append(f"{link} <- Information Disclouser detected")
        elif self.information_disclouser_robots:
            for link in self.information_disclouser_robots:
                content.append(f"{link} <- Information Disclouser detected")
        return content
    
    def information_disclouser_draw_pie(self):
            if self.information_disclouser_link:
                self.explode[1] = 0.1
            labels = ["robots.txt","error_based_disclouser","total_internal_links"]
            share = [len(self.information_disclouser_robots),len(self.information_disclouser_link),len(self.crawl_links)]

            explode = self.explode
            colors = ['red' if e > 0 else 'green' for e in explode]

            plt.style.use("ggplot")
            fig, ax = plt.subplots()
            ax.pie(x=share, explode=explode, labels=labels, autopct="%.2f%%", shadow=True, startangle=90,colors=colors)
            ax.axis('equal')
            ax.legend(loc="upper left")

            # Add a large A+ label in the center of the pie chart

            # Save the figure as an image file (e.g., PNG)
            fig.savefig('information_disclouser.png')

        

    

