from fpdf import FPDF as fp
import pandas as pd

# P is for portrait and L is for landscape
pdf = fp(orientation="P", unit='mm', format='A4')

data_frame = pd.read_csv("topic.csv")

for index, row in data_frame.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style='B', size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    pdf.line(10, 22, 200, 21)

pdf.output("output.pdf")