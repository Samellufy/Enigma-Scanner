import requests
from bs4 import BeautifulSoup
#login_url = "https://0a6a004903fb73f083c773f0003d00de.web-security-academy.net/login"

class Login_form:
    def __init__(self,login_url,s):
        self.login_url = login_url
        self.s = s
        self.detailsOfForm = {}

    def get_form(self):
        soup = BeautifulSoup(self.s.get(self.login_url).content, "html.parser")
        return soup.find_all("form")

    def form_details(self,forms):
        for form in forms:
            self.detailsOfForm = {}
            action = form.attrs.get("action")
            method = form.attrs.get("method", "get")
            inputs = []

            for input_tag in form.find_all("input"):
                input_type = input_tag.attrs.get("type", "text")
                input_name = input_tag.attrs.get("name")
                input_value = input_tag.attrs.get("value", "")
                inputs.append({
                    "type": input_type,
                    "name": input_name,
                    "value": input_value
                })
            self.detailsOfForm['action'] = action
            self.detailsOfForm['method'] = method
            self.detailsOfForm['inputs'] = inputs
            return self.detailsOfForm

    def login_form_details(self):
        return self.form_details(self.get_form())