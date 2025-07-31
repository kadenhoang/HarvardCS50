from fpdf import FPDF


pdf = FPDF()
pdf.add_page()
pdf.set_font('Times', style='I', size = 16)
pdf.cell(0, 10, text="CS50 Shirtificate", border=0, ln=1, align="C")

shirt_width = 150
page_width = pdf.w
x = (page_width - shirt_width)/ 2

pdf.image("shirtificate.png",x=x, y = 50, w=shirt_width)

