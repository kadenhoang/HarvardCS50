from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Times', style='I', size = 16)
pdf.cell(0, 10, text="CS50 Shirtificate", border=0, ln=1, align="C")
pdf.image("shirtificate.png")
