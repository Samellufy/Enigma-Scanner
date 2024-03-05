from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, title):
        super().__init__()
        self.title = title
        
        
    def header(self):
        self.image('Practice/reports/enigma-scanner-scans-web-vulnerability-high-resolution-logo-transparent.png', 10, 3, 20)
        self.set_font('helvetica', 'B', 15)
        title_w = self.get_string_width(self.title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        self.set_text_color(0, 80, 180)
        self.cell(title_w, 10, self.title, ln=1, align='C')
        self.ln(20)

    def footer(self):
        self.set_y(-15) 
        self.set_font('helvetica', 'I', 10)
        self.set_text_color(169, 169, 169)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

    # def chapter_body(self, title, content):
    #     self.set_font('times', '', 12)
    #     self.set_text_color(0, 0, 0)
    #     self.cell(0, 10, title, ln=1)
    #     for line in content:
    #         self.multi_cell(0, 10, line)
    #     self.ln()

    def first_page(self,security_content_report):
        self.image("Practice/reports/enigma-scanner-scans-web-vulnerability-high-resolution-logo-transparent.png",0,20,200)
        self.set_font('helvetica', 'BI', 20)
        self.multi_cell(0,10,"Report for the findings for the provided links",ln=True)
        for url in security_content_report:
            self.set_font('helvetica', 'BI', 12)
            self.multi_cell(0, 10, url,ln=True)

    def generate_report(self, report_for, security_report_content,pdf_name,description_filename,mitigation_filename):
        self.add_page()
        self.alias_nb_pages()
        self.set_auto_page_break(auto=True, margin=15)
        if report_for == "header_security":
            self.set_font('helvetica', '', 12)

            self.set_font('helvetica', 'B', 20)
            self.multi_cell(0,10,"Security Headers",ln=True)
            self.set_text_color(0,0,0)
            self.set_font('helvetica', '', 12)
        elif report_for == "path_traversal":
            self.set_font('helvetica', '', 12)

            self.set_font('helvetica', 'B', 20)
            self.multi_cell(0,10,"Directory Traversal",ln=True)
            self.set_text_color(0,0,0)
            self.set_font('helvetica', '', 12)
        elif report_for == "sql_injection":
            self.set_font('helvetica', '', 12)

            self.set_font('helvetica', 'B', 20)
            self.multi_cell(0,10,"Sql Injection",ln=True)
            self.set_text_color(0,0,0)
            self.set_font('helvetica', '', 12)
        elif report_for == "information_disclouser":
            self.set_font('helvetica', '', 12)

            self.set_font('helvetica', 'B', 20)
            self.multi_cell(0,10,"Information Disclouser",ln=True)
            self.set_text_color(0,0,0)
            self.set_font('helvetica', '', 12)
        with open(description_filename,'r') as txt:
            description = txt.read()
            self.multi_cell(0,10,description,ln=True)
        self.ln(10)
        self.add_page()
        
        self.set_text_color(0,0,0)
        self.set_font('helvetica', '', 12)
        if report_for == "first_page":
            self.first_page(security_report_content) 
        elif report_for == "header_security":
            self.sercurity_header_report(security_report_content)
        elif report_for == "path_traversal":
            self.path_traversal_report(security_report_content)
        elif report_for == "sql_injection":
            self.sql_injection_report(security_report_content)
        elif report_for == "information_disclouser":
            self.information_disclouser_report(security_report_content)
        elif report_for == "last_page":
            self.last_page()
        
        self.ln(10)
        self.add_page()
        self.set_text_color(0,0,0)
        self.set_font('helvetica', 'B', 20)
        self.multi_cell(0,10,"Mitigation: ",ln=True)
        self.set_text_color(0,0,0)
        self.set_font('helvetica', '', 12)
        with open(mitigation_filename,'r') as txt:
            mitigation = txt.read()
            self.multi_cell(0,10,mitigation,ln=True)
    
    def first_page(self,security_content_report):
                self.add_page()
                self.alias_nb_pages()
                self.set_auto_page_break(auto=True, margin=15)
                self.image("Practice/reports/enigma-scanner-scans-web-vulnerability-high-resolution-logo-transparent.png",30,20,150)
                self.set_font('helvetica', 'BI', 20)
                self.ln(150)
                self.set_text_color(0,80,180)
                self.multi_cell(0,10,"Report for the findings of the link",ln=True,align='C')
                for url in security_content_report:
                    self.set_font('helvetica', 'BI', 12)
                    self.multi_cell(0, 10, url,ln=True,align='C')


    def sercurity_header_report(self,security_report_content):
        missing_headers = []
        self.set_text_color(255,0,0)
        self.set_font('helvetica', 'BI', 20)
        self.multi_cell(0,10,"Security Misconfiguration detected: ",'Bold',ln=True)
        self.set_text_color(0,0,0)
        self.set_font('helvetica', '', 12)

        for line in security_report_content:
                if "A+" in line:
                    self.set_font('helvetica', 'BI', 12)
                    self.set_text_color(128,255,0) 
                elif "A" in line:
                    self.set_font('helvetica', 'BI', 12)
                    self.set_text_color(0,153,0) 
                elif "B" in line:
                    self.set_font('helvetica', 'BI', 12)
                    self.set_text_color(204,204,0)
                elif "C" in line:
                    self.set_font('helvetica', 'BI', 12)
                    self.set_text_color(153,153,0)
                elif "D" in line:
                    self.set_font('helvetica', 'BI', 12)
                    self.set_text_color(255,128,0) 
                elif "E" in line:
                    self.set_font('helvetica', 'BI', 12)
                    self.set_text_color(153,76,0)  
                elif "F" in line:
                    self.set_font('helvetica', 'BI', 12)
                    self.set_text_color(255,0,0) 
                if "risk" in line:
                    self.set_font('helvetica', '', 12)
                    self.set_text_color(255, 0, 0)
                    self.multi_cell(0, 10, line,ln=True)
                else:
                    self.multi_cell(0, 10, line,ln=True)
        self.image("security_header_pie.png",0,130,150)
                    
    def path_traversal_report(self,security_content_report):
        self.set_text_color(255,0,0)
        self.set_font('helvetica', 'BI', 20)
        self.multi_cell(0,10,"Directory Traversal detected: ",ln=True)
        self.set_text_color(0,0,0)
        self.set_font('helvetica', '', 12)
        for line in security_content_report:
            if "URL" not in line:
                self.set_text_color(255,0,0)
                self.multi_cell(0,10,line,ln=True)
            else:
                self.multi_cell(0,10,line,ln=True)

        self.image("path_traversal_pie.png",0,130,150)
    
    def sql_injection_report(self,security_content_report):
        self.set_text_color(255,0,0)
        self.set_font('helvetica', 'BI', 20)
        self.multi_cell(0,10,"Sql injection detected: ",ln=True)
        self.set_text_color(0,0,0)
        self.set_font('helvetica', '', 12)
        print(security_content_report)
        for line in security_content_report:
            if "Target" not in line:
                self.set_text_color(255,0,0)
                self.multi_cell(0,10,line,ln=True)
            else:
                self.multi_cell(0,10,line,ln=True)

        self.image("sql_injection_pie.png",0,130,150)

    def information_disclouser_report(self,security_content_report):
        self.set_text_color(255,0,0)
        self.set_font('helvetica', 'BI', 20)
        self.multi_cell(0,10,"Information Disclouser detected: ",ln=True)
        self.set_text_color(0,0,0)
        self.set_font('helvetica', '', 12)
        print(security_content_report)
        for line in security_content_report:
            if "Target" not in line:
                self.set_text_color(255,0,0)
                self.multi_cell(0,10,line,ln=True)
            else:
                self.multi_cell(0,10,line,ln=True)

        self.image("information_disclouser.png",0,130,150)
        
    def last_page(self):
            self.add_page()
            self.alias_nb_pages()
            self.set_auto_page_break(auto=True, margin=15)
            self.set_font('helvetica', 'B', 50)
            self.ln(130)
            self.multi_cell(0,10,"Thank you",ln=True,align='C')
    
    def done_generating_report(self,pdf_name):
        self.output("Practice/reports/"+pdf_name)

    
                

    
            
        