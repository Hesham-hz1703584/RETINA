from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 20)
        self.cell(0, 10, 'Diagnosis Report', border=False, align='C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 10)
        self.cell(0, 10, f'Page {self.page_no()}', border=False, align='C')


def GeneratePdf():
    pdf = PDF('p', 'mm', 'A4')
    pdf.add_page()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_font('helvetica', '', 16)
    pdf.output('pdf_1.pdf')


def readReports(Reports, pdf):
    textarr = []
    for i in range(0, len(Reports)):
        text = f'\nCase:{i + 1}' + "\n\n" + Reports[i][0] + "\n\n" + Reports[i][1] + "\n\n" + Reports[i][2] + "\n"
        textarr.append(text)
        continue
    for y in range(0, len(textarr)):
        pdf.multi_cell(0, 5, textarr[y] + '\n', 1)
