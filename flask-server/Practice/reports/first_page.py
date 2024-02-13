from fpdf import FPDF
class first_PDF(FPDF):
    def __init__(self, title):
        super().__init__()
        self.title = title
        
        
    def header(self):
        self.image('reports/enigma-scanner-scans-web-vulnerability-high-resolution-logo-transparent.png', 10, 3, 20)
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

    def chapter_body(self, title, content):
        self.set_font('times', '', 12)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, title, ln=1)
        for line in content:
            self.multi_cell(0, 10, line)
        self.ln()

    def first_page(self,security_content_report):
            self.image("reports/enigma-scanner-scans-web-vulnerability-high-resolution-logo-transparent.png",30,20,150)
            self.set_font('helvetica', 'BI', 20)
            self.ln(150)
            self.set_text_color(0,80,180)
            self.multi_cell(0,10,"Report for the findings of the link",ln=True,align='C')
            for url in security_content_report:
                self.set_font('helvetica', 'BI', 12)
                self.multi_cell(0, 10, url,ln=True,align='C')
    
    def generate_report(self, report_for, security_report_content,pdf_name,):
        self.add_page(orientation='P', format='Letter')
        self.alias_nb_pages()
        self.set_auto_page_break(auto=True, margin=15)
        if report_for == "first_page":
            self.first_page(security_report_content)
        if report_for == "last_page":
            self.set_font('helvetica', 'B', 50)
            self.ln(130)
            self.multi_cell(0,10,"Thank you",ln=True,align='C')
            self.output("reports/"+pdf_name)

        
