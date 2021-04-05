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
class Result():
    Obj = DCF()
    pdf = FPDF()

    # ## Write Results to file
    destination_path = os.path.dirname(__file__)
    destination_path = os.path.join(destination_path, "valuations.txt")

    with open(destination_path, 'w') as val:
        val.write("--------------------------------------------------------------------\n")
        val.write("-----------------------------VALUATION------------------------------\n")
        val.write("--------------------------------------------------------------------\n\n")

        # Solvency Ratio
        val.write("1) SOLVENCY RATIO: \n")
        if Obj.debt2equity[0] < 1:
            val.write("The Company has a GOOD Debt to Equity ratio\n")
        else:
            val.write("The Company has a BAD Debt to Equity ratio\n")
        val.write("Debt to Equity Ratio = %f \n" % Obj.debt2equity[0])

        if Obj.int_cov_ratio[0] > 1:
            val.write("The Company has a GOOD Interest Coverage Ratio\n")
        else:
            val.write("The Company has a BAD Interest Coverage Ratio\n")
        val.write("Interest Coverage Ratio = %f \n\n" % Obj.int_cov_ratio[0])

        # Liquidity Ratio
        val.write("2) LIQUIDITY RATIO: \n")
        if Obj.cur_ratio[0] > 2:

            val.write("The Company has a GOOD Current Ratio\n")
        else:
            val.write("The Company has a BAD Current Ratio\n")

        if Obj.cshratio[0] > 1:
            val.write("The Company has a GOOD Cash Ratio\n")
        else:
            val.write("The Company has a BAD Cash Ratio\n")
        val.write("Current Ratio = %f \n" % Obj.cur_ratio[0])
        val.write("Cash Ratio = %f \n" % Obj.cshratio[0])

        if Obj.op_cashflow_ratio[0] > 1:
            val.write("The Company has a GOOD Operating Cashflow Ratio\n")
        else:
            val.write("The Company has a BAD Operating Cashflow Ratio\n")
        val.write("Operating Cashflow Ratio = %f \n" % Obj.op_cashflow_ratio[0])

        if Obj.inv_turnover_ratio[0] > 5:
            val.write("The Company has a GOOD Inventory Turnover Ratio\n")
        else:
            val.write("The Company has a BAD Inventory Turnover Ratio\n")
        val.write("Inventory Turnover Ratio = %f \n\n" % Obj.inv_turnover_ratio[0])

        # Profitability Ratio
        val.write("3) Profitability RATIO: \n")
        if Obj.opr_income_margin[0] > 15:
            val.write("The Company has a GOOD Operating Income Margin\n")
        else:
            val.write("The Company has a BAD Operating Income Margin\n")
        val.write("Operating Income Margin = %f \n" % Obj.opr_income_margin[0])

        if Obj.net_prft_margin[0] > 15:
            val.write("The Company has a GOOD Net Profit Margin\n")
        else:
            val.write("The Company has a BAD Net Profit Margin\n")
        val.write("Net Profit Margin = %f \n" % Obj.net_prft_margin[0])

        if Obj.roe[0] > 10:
            val.write("The Company has a GOOD Return on Equity\n")
        else:
            val.write("The Company has a BAD Return on Equity\n")
        val.write("Return on Equity = %f \n" % Obj.roe[0])

        if Obj.roa[0] > 10:
            val.write("The Company has a GOOD Return on Assets\n")
        else:
            val.write("The Company has a BAD Return on Assets\n")
        val.write("Return on Assets = %f \n\n" % Obj.roa[0])


        # Intrinsic Value Calculation
        val.write("--------------------------------------------------------------------\n")
        val.write("----------------------Intrinsic Value Calculation-------------------\n")
        val.write("--------------------------------------------------------------------\n\n")
        val.write("WACC Calculation \n")
        val.write("WACC calculated as = %f \n" % Obj.WACC)

        # pdf.add_page()
        # pdf.set_font('Arial', 'B', 16)
        #
        # pdfwrite = open("valuations.txt", "r")
        # for items in pdfwrite:
        #     pdf.cell(200, 10,txt = items,ln = 1)
        # pdfwrite.close()
        # pdf.output('Valuations.pdf', 'F')
