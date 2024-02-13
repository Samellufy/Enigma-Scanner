import os
from Crawler import Crawler
from Payloads.page_type_check import PageCheck
from attack.sql_url import Usql
from scrapping.Login import Login_form
from attack.sql_login_bypass import Lsqli
import requests
import urllib.parse as urlparse
from Scrapping import Scrapping
from attack.sql_blind import Blind_conditional_sqli
from attack.sql_time_based import Time_based_sqli
# from attack.header_security import HeaderSecurity
from attack.header_security import HeaderSecurity
from attack.information_disclouser import InformationDisclouser
from attack.path_traverse import DirectoryTraversal
# from reports.reports import ComprehensiveReport
from reports.reports import PDF
from reports.sqli_pie import SqlPie
from reports.merge_all_reports import merge_pdfs
from reports.first_page import first_PDF

h_security = 0

s = requests.Session()

target_url = "https://mangakakalot.com"



crawl = Crawler(target_url)
crawl_links = crawl.start_crawling()

print(crawl_links)


# page_check = PageCheck(crawl_links)
# link = page_check.is_login_page()

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print(files)

# sql_injection_report_content = []
# types_of_sql_injections = [0,0,0]

# first_page_report = [target_url]

# rgeneration = PDF("EnigmaScanner")
# frgeneration = first_PDF("EnigmaScanner")
# # frgeneration.generate_report("first_page",first_page_report,"first.pdf")
# rgeneration.first_page(first_page_report)


# # #---------------------------------Path Traversal------------------------------------------
# print("Checking for pathtraversal")
# pathtraverse = DirectoryTraversal(target_url,crawl_links)
# pathtraverse.path_traversal()
# directory_traversal_content_report = pathtraverse.get_security_report_content()
# if directory_traversal_content_report:
#     pathtraverse.traversal_draw_pie()
#     rgeneration.generate_report("path_traversal",directory_traversal_content_report,"path_traversal.pdf","reports/report_text/path_traversal.txt","reports/mitigations/path_traversal_mitigations.txt")
# #---------------------------------------SQL INJECTION---------------------------------------------
# # Check for url based injection
# print("Checking for sql injection")
# usqli = Usql(crawl_links,target_url)
# usqli.url_sqli()
# url_sql_injection = usqli.get_security_report_content()
# print(url_sql_injection)
# if url_sql_injection:
#     types_of_sql_injections[0] = 0.1
#     sql_injection_report_content = url_sql_injection
# print(sql_injection_report_content)
# #
# # Checks for the blind contitional response injection
# BCon = Blind_conditional_sqli(target_url,s)
# BCon.check_for_blind_conditional_sqli()
# sql_blind_error_based = BCon.get_security_report_content()
# if sql_blind_error_based:
#     types_of_sql_injections[1] = 0.1
#     sql_injection_report_content = sql_blind_error_based
    


# # Checks for the blind time based sql injection
# time_based_sqli = Time_based_sqli(target_url,s)
# time_based_sqli.check_for_time_based_sqli()
# sql_time_based = time_based_sqli.get_security_report_content()
# if sql_time_based:
#     types_of_sql_injections[2] = 0.1
#     sql_injection_report_content = sql_time_based

# # # Sql report generation
# if sql_injection_report_content:
#     rgeneration.generate_report("sql_injection",sql_injection_report_content,"sql_injection.pdf","reports/report_text/sql_injection.txt","reports/mitigations/sql_injection_mitigation.txt")
#     sql_pie = SqlPie(types_of_sql_injections)
#     sql_pie.sql_injection_draw_pie()


# #-------------------------------------------------------------------------------------------

# #----------------------------Header Security------------------------------------------------
# print("Checking for security headers")
# hsecurity = HeaderSecurity(target_url)
# hsecurity.check_headers_security()
# security_report_content = hsecurity.get_security_report_content()
# if security_report_content:
#     hsecurity.draw_pie_chart()
#     rgeneration.generate_report("header_security",security_report_content,"head_security.pdf","reports/report_text/security_header.txt","reports/mitigations/security_header_mitigation.txt")




# #--------------------------------Information Disclosure------------------------------------
# print("Checking for information disclouser")
# check_information_disclouser = InformationDisclouser(target_url,crawl_links)
# check_information_disclouser.check_for_robotstxt_file()
# check_information_disclouser.error_based()
# information_content_report = check_information_disclouser.get_security_report_content()
# if information_content_report:
#     check_information_disclouser.information_disclouser_draw_pie()
#     rgeneration.generate_report("information_disclouser",information_content_report,"information.pdf","reports/report_text/information_disclouser.txt","reports/mitigations/information_disclouser_mitigation.txt")

# #----------------------------------Report Generation---------------------------------------
# # frgeneration.generate_report("last_page",first_page_report,"last_page.pdf")
# print("Generating report")
# rgeneration.last_page()
# rgeneration.done_generating_report("completed_report.pdf")
# merge_pdfs("reports","merge.pdf")


