import requests
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class HeaderSecurity:
    def __init__(self, target_url):
        self.target_url = target_url
        self.header_list = ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options", "Referrer-Policy", "Permissions-Policy"]
        self.headers = {}
        self.header_required = 6
        self.header_missing = []
        self.header_present = []
        self.get_headers()

    def get_headers(self):
        header = requests.get(self.target_url).headers
        self.headers = header

    def check_headers_security(self):
        for missing_header in self.header_list:
            if missing_header not in self.headers:
                self.header_missing.append(missing_header)
            else:
                self.header_present.append(missing_header)

    def get_security_report_content(self):
        content = []
        content.append(f"Target URL: {self.target_url}")
        
        if (self.header_required - len(self.header_missing)) == 0:
            content.append("Score: A+")
        elif (self.header_required - len(self.header_missing)) == 1:
            content.append("Score: A")
        elif (self.header_required - len(self.header_missing)) == 2:
            content.append("Score: B")
        elif (self.header_required - len(self.header_missing)) == 3:
            content.append("Score: C")
        elif (self.header_required - len(self.header_missing)) == 4:
            content.append("Score: D")
        elif (self.header_required - len(self.header_missing)) == 5:
            content.append("Score: E")
        elif (self.header_required - len(self.header_missing)) == 6:
            content.append("Score: F")


        for missing_header in self.header_missing:
            if missing_header == "Strict-Transport-Security":
                content.append("High risk of man-in-the-middle attack")
            elif missing_header == "Content-Security-Policy":
                content.append("High risk of xss and data injection attacks")
            elif missing_header == "X-Frame-Options":
                content.append("High risk of clickjacking injection attacks")
            elif missing_header == "X-Content-Type-Options":
                content.append("High risk of MIME-based attacks")
            elif missing_header == "Referrer-Policy":
                content.append("User privacy is at risk")
            elif missing_header == "Permissions-Policy":
                content.append("Security policy not set for features like camera,microphone and more")
            # Add other statements for missing headers

        return content

# Example usage
