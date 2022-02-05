#pdf maker using python 
#requirements :- pip install fpdf (command on terminal of your IDE)
# can use latest version fpdf2 


#import module
from fpdf import FPDF

#assign FPDF module
#variable class
pdf= FPDF()

#adds page 
pdf.add_page()

#adds font
pdf.set_font("Arial", size = 15)

#adds text(cell1)
pdf.cell(200, 10, txt = "ERICA BASTYAV DSOUZA",
         ln = 1, align = 'C')
#adds text(cell2)
pdf.cell(200, 10, txt="IT ENGINEERING STUDENT.",
         ln=2, align='C')

#nomenclature to save the PDF
pdf.output("info.pdf")
