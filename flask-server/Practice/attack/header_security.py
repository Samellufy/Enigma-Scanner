import requests
import matplotlib.pyplot as plt

class HeaderSecurity:
    def __init__(self,target_url):
        self.target_url = target_url
        self.header_list = ["Strict-Transport-Security","Content-Security-Policy","X-Frame-Options","X-Content-Type-Options","Referrer-Policy","Permissions-Policy"]
        self.headers = {}
        self.header_required = 6
        self.header_missing = []
        self.explode = [0,0,0,0,0,0]
        self.get_headers()

    def get_headers(self):
        header = requests.get(self.target_url).headers
        self.headers = header

    def check_headers_security(self):
        for missing_header in self.header_list:
            if missing_header not in self.headers:
                if missing_header == "Strict-Transport-Security":
                        self.header_missing.append(missing_header)
                        self.explode[0] = 0.1
                elif missing_header == "Content-Security-Policy":
                        self.header_missing.append(missing_header)
                        self.explode[1] = 0.1
                elif missing_header == "X-Frame-Options":
                        self.header_missing.append(missing_header)
                        self.explode[2] = 0.1
                elif missing_header == "X-Content-Type-Options":
                    self.header_missing.append(missing_header)
                    self.explode[3] = 0.1
                # deepcode ignore IdenticalBranches: <please specify a reason of ignoring this>
                elif missing_header == "Referrer-Policy":
                    self.header_missing.append(missing_header)
                    self.explode[4] = 0.1
                elif missing_header == "Permissions-Policy":
                    self.header_missing.append(missing_header)
                    self.explode[5] = 0.1
                     

    def get_security_report_content(self):
        print(self.header_missing)
        content = []
        content.append(f"Target URL: {self.target_url}")
        print(self.header_required - len(self.header_missing))
        
        if (self.header_required - len(self.header_missing)) == 0:
            content.append("Score: F")
        elif (self.header_required - len(self.header_missing)) == 1:
            content.append("Score: E")
        elif (self.header_required - len(self.header_missing)) == 2:
            content.append("Score: D")
        elif (self.header_required - len(self.header_missing)) == 3:
            content.append("Score: C")
        elif (self.header_required - len(self.header_missing)) == 4:
            content.append("Score: B")
        elif (self.header_required - len(self.header_missing)) == 5:
            content.append("Score: A")
        elif (self.header_required - len(self.header_missing)) == 6:
            content.append("Score: A+")


        for missing_header in self.header_missing:
            if missing_header == "Strict-Transport-Security":
                content.append(f"RISK: {missing_header} -> High risk of man-in-the-middle attacks")
            elif missing_header == "Content-Security-Policy":
                content.append(f"RISK: {missing_header} -> High risk of xss and data injection attacks")
            elif missing_header == "X-Frame-Options":
                content.append(f"RISK: {missing_header} -> High risk of clickjacking injection attacks")
            elif missing_header == "X-Content-Type-Options":
                content.append(f"RISK: {missing_header} -> High risk of MIME-based attacks")
            elif missing_header == "Referrer-Policy":
                content.append(f"RISK: {missing_header} -> User privacy is at risk")
            elif missing_header == "Permissions-Policy":
                content.append(f"RISK: {missing_header} -> Security policy not set for features like camera,microphone and more")

        return content
    def draw_pie_chart(self):

        labels = ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options", "Referrer-Policy", "Permissions-Policy"]
        share = [1, 2, 3, 4, 5, 6]

        explode = self.explode
        colors = ['red' if e > 0 else 'green' for e in explode]

        plt.style.use("ggplot")
        fig, ax = plt.subplots()
        ax.pie(x=share, explode=explode, labels=labels, shadow=True, startangle=90, colors=colors)

        # Add a large A+ label in the center of the pie chart
        if(len(self.header_missing)) == 0:
            ax.text(0, 0, 'A+', fontsize=40, color='black', ha='center', va='center')
        elif(len(self.header_missing)) == 1:
            ax.text(0, 0, 'A', fontsize=40, color='black', ha='center', va='center')
        elif(len(self.header_missing)) == 2:
            ax.text(0, 0, 'B', fontsize=40, color='black', ha='center', va='center') 
        elif(len(self.header_missing)) == 3:
            ax.text(0, 0, 'C', fontsize=40, color='black', ha='center', va='center')   
        elif(len(self.header_missing)) == 4:
            ax.text(0, 0, 'D', fontsize=40, color='black', ha='center', va='center')
        elif(len(self.header_missing)) == 5:
            ax.text(0, 0, 'E', fontsize=40, color='black', ha='center', va='center')
        elif(len(self.header_missing)) == 6:
            ax.text(0, 0, 'F', fontsize=40, color='black', ha='center', va='center')

        # Save the figure as an image file (e.g., PNG)
        fig.savefig('security_header_pie.png')



             
    
        
