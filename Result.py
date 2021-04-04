"""
Author : Bharani Deepak
Info   : This class writes the valuation results to a file
"""
from dataclasses import dataclass
from fpdf import FPDF
from DCF import *
from Base import *


logging.basicConfig(filename="logfile.log", level=logging.INFO,
                    format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',
                    datefmt='[%d/%m/%Y] (%H:%M:%S)', filemode='w')

mainlogger = logging.getLogger(__name__)
mainlogger.info("Stock Valuation started")

@dataclass
class Result(FPDF):
    Obj = DCF()

    # ## Write Results to file
    destination_path = os.path.dirname(__file__)
    destination_path = os.path.join(destination_path, "valuations.txt")

    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Line break
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')


    def print_chapter(self, num, title, name):
        pdf = FPDF()
        FPDF().add_page()
        self.chapter_title(num, title)
        #self.chapter_body(name)

    def chapter_title(self, num, label):
        pdf = FPDF()

        pdf.add_page()
        # Arial 12
        pdf.set_font('Arial', '', 12)
        # Background color
        pdf.set_fill_color(200, 220, 255)
        # Title
        pdf.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        pdf.ln(4)

    def chapter_body(self, name):
        pdf = FPDF()

        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')

        # Times 12
        pdf.set_font('Times', '', 12)
        pdf.add_page()
        # Output justified text
        pdf.multi_cell(0, 5, txt)
        # Line break
        pdf.ln()
        # Mention in italics
        pdf.set_font('', 'I')
        pdf.cell(0, 5, '(end of excerpt)')

    pdf = FPDF()

    # with open(destination_path, 'w') as val:
    #     # val.write("--------------------------------------------------------------------\n")
    #     val.write("-----------------------------VALUATION------------------------------\n")
    #     val.write("--------------------------------------------------------------------\n\n")
    #
    #     # Solvency Ratio
    #     val.write("1) SOLVENCY RATIO: \n")
    #     if Obj.debt2equity[0] < 1:
    #         val.write("The Company has a GOOD Debt to Equity ratio\n")
    #     else:
    #         val.write("The Company has a BAD Debt to Equity ratio\n")
    #     val.write("Debt to Equity Ratio = %f \n" % Obj.debt2equity[0])
    #
    #     if Obj.int_cov_ratio[0] > 1:
    #         val.write("The Company has a GOOD Interest Coverage Ratio\n")
    #     else:
    #         val.write("The Company has a BAD Interest Coverage Ratio\n")
    #     val.write("Interest Coverage Ratio = %f \n\n" % Obj.int_cov_ratio[0])
    #
    #     # Liquidity Ratio
    #     val.write("2) LIQUIDITY RATIO: \n")
    #     if Obj.cur_ratio[0] > 2:
    #
    #         val.write("The Company has a GOOD Current Ratio\n")
    #     else:
    #         val.write("The Company has a BAD Current Ratio\n")
    #     val.write("Current Ratio = %f \n" % Obj.cur_ratio[0])
    #
    #     if Obj.cshratio[0] > 1:
    #         val.write("The Company has a GOOD Cash Ratio\n")
    #     else:
    #         val.write("The Company has a BAD Cash Ratio\n")
    #     val.write("Cash Ratio = %f \n" % Obj.cshratio[0])
    #
    #     if Obj.op_cashflow_ratio[0] > 1:
    #         val.write("The Company has a GOOD Operating Cashflow Ratio\n")
    #     else:
    #         val.write("The Company has a BAD Operating Cashflow Ratio\n")
    #     val.write("Operating Cashflow Ratio = %f \n" % Obj.op_cashflow_ratio[0])
    #
    #     if Obj.inv_turnover_ratio[0] > 5:
    #         val.write("The Company has a GOOD Inventory Turnover Ratio\n")
    #     else:
    #         val.write("The Company has a BAD Inventory Turnover Ratio\n")
    #     val.write("Inventory Turnover Ratio = %f \n\n" % Obj.inv_turnover_ratio[0])
    #
    #     # Profitability Ratio
    #     val.write("3) Profitability RATIO: \n")
    #     if Obj.opr_income_margin[0] > 15:
    #         val.write("The Company has a GOOD Operating Income Margin\n")
    #     else:
    #         val.write("The Company has a BAD Operating Income Margin\n")
    #     val.write("Operating Income Margin = %f \n" % Obj.opr_income_margin[0])
    #
    #     if Obj.net_prft_margin[0] > 15:
    #         val.write("The Company has a GOOD Net Profit Margin\n")
    #     else:
    #         val.write("The Company has a BAD Net Profit Margin\n")
    #     val.write("Net Profit Margin = %f \n" % Obj.net_prft_margin[0])
    #
    #     if Obj.roe[0] > 10:
    #         val.write("The Company has a GOOD Return on Equity\n")
    #     else:
    #         val.write("The Company has a BAD Return on Equity\n")
    #     val.write("Return on Equity = %f \n" % Obj.roe[0])
    #
    #     if Obj.roa[0] > 10:
    #         val.write("The Company has a GOOD Return on Assets\n")
    #     else:
    #         val.write("The Company has a BAD Return on Assets\n")
    #     val.write("Return on Assets = %f \n\n" % Obj.roa[0])
    #
    #
    #     # Intrinsic Value Calculation
    #     val.write("--------------------------------------------------------------------\n")
    #     val.write("----------------------Intrinsic Value Calculation-------------------\n")
    #     val.write("--------------------------------------------------------------------\n\n")
    #     val.write("WACC Calculation \n")
    #     val.write("WACC calculated as = %f \n" % Obj.WACC)