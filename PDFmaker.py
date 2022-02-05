#pdf maker using python 
#requirements :- pip install fpdf (command on terminal of your IDE)
# can use latest version fpdf2 


#import module
from fpdf import FPDF

pdf= FPDF()

pdf.add_page()
pdf.set_font("Arial", size = 15)
pdf.cell(200, 10, txt = "ERICA BASTYAV DSOUZA",
         ln = 1, align = 'C')
pdf.cell(200, 10, txt="IT ENGINEERING STUDENT.",
         ln=2, align='C')
pdf.output("info.pdf")
