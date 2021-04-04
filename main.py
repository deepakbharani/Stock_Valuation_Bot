from DCF import *
from Result import *
from fpdf import FPDF

if __name__ == "__main__":

    # Creating object for class DCF
    obj = Result()

    # Generate PDF result of the Valuation
    #pdf.set_title('Stock Valuation')
    #pdf.set_author('Bharani Deepak')

    obj.print_chapter(num=1, title='Solvency Ratio', name='valuations.txt')
    FPDF().output('valuations.pdf')