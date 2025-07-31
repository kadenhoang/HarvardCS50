from fpdf import FPDF

name = input("Name:")
#make a white page with text on the middle top
pdf = FPDF()
pdf.add_page()
pdf.set_font('Times', style='B', size = 40)
pdf.cell(0, 30, "CS50 Shirtificate", border=0, ln=1, align="C")

#add the shirt and center it
shirt_width = 150
page_width = pdf.w
x = (page_width - shirt_width)/ 2
y = 50
pdf.image("shirtificate.png",x=x, y=y, w=shirt_width)

#write white text on top of the shirt
pdf.set_font('Times', style='I', size = 18)
pdf.set_text_color(212,175,55)

text_x = pdf.get_x()
text_y = y + 40
pdf.set_xy(x, text_y)

pdf.cell(shirt_width, 10, f"{name} took CS50", align = "C")
pdf.output("shirttificate_wt_text.pdf")
