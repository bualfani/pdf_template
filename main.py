from fpdf import FPDF as fp
import pandas as pd

# P is for portrait and L is for landscape
pdf = fp(orientation="P", unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

data_frame = pd.read_csv("topic.csv")

for index, row in data_frame.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style='B', size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    pdf.line(10, 22, 200, 21)

    pdf.ln(265)
    # set the footer
    pdf.set_font(family="Times", style='I', size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')



    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # set the footer
        pdf.ln(278)

        pdf.set_font(family="Times", style='I', size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

pdf.output("output.pdf")