from flask import Flask,jsonify,request,send_file
from flask_cors import CORS
from crawler import Crawler
import json
import os
# from Practice.Crawler import Crawler
from Practice.Payloads.page_type_check import PageCheck
from Practice.attack.sql_url import Usql
# from Practice.scrapping.Login import Login_form
# from Practice.attack.sql_login_bypass import Lsqli
import requests
import urllib.parse as urlparse
from Practice.Scrapping import Scrapping
from Practice.attack.sql_blind import Blind_conditional_sqli
from Practice.attack.sql_time_based import Time_based_sqli
# from attack.header_security import HeaderSecurity
from Practice.attack.header_security import HeaderSecurity
from Practice.attack.information_disclouser import InformationDisclouser
from Practice.attack.path_traverse import DirectoryTraversal
# from reports.reports import ComprehensiveReport
from Practice.reports.reports import PDF
from Practice.reports.sqli_pie import SqlPie
from Practice.reports.merge_all_reports import merge_pdfs
from Practice.reports.first_page import first_PDF


h_security = 0

s = requests.Session()

# target_url = "https://mangakakalot.com/"



# crawl = Crawler(target_url)
# crawl_links = crawl.start_crawling()

# print(crawl_links)


# page_check = PageCheck(crawl_links)
# link = page_check.is_login_page()

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print(files)







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



# from data import Data

app = Flask(__name__)
CORS(app)
@app.route("/scanner")
def members():
    global scanning_in_progess
    try:
        target_url = request.args.get("url", "")
        sql_injection_report_content = []
        types_of_sql_injections = [0,0,0]
        rgeneration = PDF("EnigmaScanner")
        first_page_report = [target_url]
        rgeneration.first_page(first_page_report)
        
        # Crawl the target URL
        crawl = Crawler(target_url)
        crawl_links = crawl.start_crawling()
        print(crawl_links)

        # Check for information disclosure
        check_information_disclouser = InformationDisclouser(target_url, crawl_links)
        check_information_disclouser.check_for_robotstxt_file()
        information_content_report = check_information_disclouser.get_security_report_content()

        # Check for security headers
        print("Checking for security headers")
        hsecurity = HeaderSecurity(target_url)
        hsecurity.check_headers_security()
        security_report_content = hsecurity.get_security_report_content()

        # # #---------------------------------Path Traversal------------------------------------------
        # print("Checking for pathtraversal")
        # pathtraverse = DirectoryTraversal(target_url,crawl_links)
        # print("continuing for pt checking")
        # pathtraverse.path_traversal()
        # directory_traversal_content_report = pathtraverse.get_security_report_content()
        # if directory_traversal_content_report:
            # pathtraverse.traversal_draw_pie()
#     rgeneration.generate_report("path_traversal",directory_traversal_content_report,"path_traversal.pdf","reports/report_text/path_traversal.txt","reports/mitigations/path_traversal_mitigations.txt")

        #---------------------------------------SQL INJECTION---------------------------------------------
# # Check for url based injection
        print("Checking for sql injection")
        usqli = Usql(crawl_links,target_url)
        usqli.url_sqli()
        url_sql_injection = usqli.get_security_report_content()
        print(url_sql_injection)
        if url_sql_injection:
            types_of_sql_injections[0] = 0.1
            sql_injection_report_content.extend(url_sql_injection)
        print(sql_injection_report_content)
# #
# # Checks for the blind contitional response injection
        BCon = Blind_conditional_sqli(target_url,s)
        BCon.check_for_blind_conditional_sqli()
        sql_blind_error_based = BCon.get_security_report_content()
        if sql_blind_error_based:
            types_of_sql_injections[1] = 0.1
            sql_injection_report_content.extend(sql_blind_error_based)
    


# # Checks for the blind time based sql injection
        time_based_sqli = Time_based_sqli(target_url,s)
        time_based_sqli.check_for_time_based_sqli()
        sql_time_based = time_based_sqli.get_security_report_content()
        if sql_time_based:
            types_of_sql_injections[2] = 0.1
            sql_injection_report_content.extend(sql_time_based)

# # # Sql report generation
        if sql_injection_report_content:
            rgeneration.generate_report("sql_injection",sql_injection_report_content,"sql_injection.pdf","Practice/reports/report_text/sql_injection.txt","Practice/reports/mitigations/sql_injection_mitigation.txt")
            sql_pie = SqlPie(types_of_sql_injections)
            sql_pie.sql_injection_draw_pie()
        
            rgeneration.generate_report("header_security",security_report_content,"head_security.pdf","Practice/reports/report_text/security_header.txt","Practice/reports/mitigations/security_header_mitigation.txt")

        # Prepare the response data
        response_data = {"crawl_links": crawl_links}

        # Include vulnerability information in the response if available
        if information_content_report!=[]:
            response_data["information_disclouser"] = information_content_report

        if security_report_content!=[]:
            hsecurity.draw_pie_chart()
            response_data["security_headers"]=security_report_content
            rgeneration.generate_report("header_security",security_report_content,"head_security.pdf","Practice/reports/report_text/security_header.txt","Practice/reports/mitigations/security_header_mitigation.txt")
        
        #Sql injection 

        if url_sql_injection!=[]:
            types_of_sql_injections[0] = 0.1
            response_data["url_based_sql_injection"]=url_sql_injection

        if sql_blind_error_based!=[]:
            types_of_sql_injections[1] = 0.1
            response_data["blind_error_based"]=sql_blind_error_based

        if sql_time_based!=[]:
            types_of_sql_injections[2] = 0.1
            response_data["sql_blind_time_based"]=sql_time_based

        #Path Traversal
        # if directory_traversal_content_report:
        #     response_data["path_traversal"]=directory_traversal_content_report
        
        
        print("Generating report")
        rgeneration.last_page()
        rgeneration.done_generating_report("completed_report.pdf")
        # Convert the dictionary to a JSON string
        response_str = jsonify(response_data)

        return response_str

    except Exception as e:
        print("Exception:", e)
        return "An error occurred."
    
@app.route("/download-report")
def download_report():
    try:
        report_path = "Practice/reports/completed_report.pdf"
        return send_file(report_path)
    except Exception as e:
        print("Exception:",e)
        return "An error occoured"


if __name__ == "__main__":
    app.run(debug=True)
