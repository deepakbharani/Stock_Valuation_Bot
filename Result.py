"""
Author : Bharani Deepak
Info   : This class writes the valuation results to a file
"""
from dataclasses import dataclass
from fpdf import FPDF
from Valuation import *
from Base import *


logging.basicConfig(filename="logfile.log", level=logging.INFO,
                    format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',
                    datefmt='[%d/%m/%Y] (%H:%M:%S)', filemode='w')

mainlogger = logging.getLogger(__name__)
mainlogger.info("Stock Valuation started")

@dataclass
class Result():
    Obj = Valuation()
    pdf = FPDF()

    # ## Write Results to file
    destination_path = os.path.dirname(__file__)
    destination_path = os.path.join(destination_path, "valuations.txt")

    with open(destination_path, 'w') as val:
        val.write("--------------------------------------------------------------------\n")
        val.write("-----------------------------VALUATION------------------------------\n")
        val.write("--------------------------------------------------------------------\n\n")

        # Stock Details
        val.write(f"STOCK DETAILS\n")
        val.write(f"Stock Ticker - {Obj.stock_ticker}\n")
        val.write(f"Stock Beta - {Obj.beta}\n")
        val.write(f"Market Capitalisation - {Obj.marketcap}\n")
        val.write(f"Current Market Price - {Obj.cmp}\n")
        val.write(f"Shares Outstanding - {Obj.sharesoutstanding}\n\n")

        # Solvency Ratio
        val.write("1) SOLVENCY RATIO: \n")
        if Obj.debt2equity[-1] < 1:
            val.write("The Company has a GOOD Debt to Equity ratio\n")
        else:
            val.write("The Company has a BAD Debt to Equity ratio\n")
        val.write("Debt to Equity Ratio = %f \n" % Obj.debt2equity[-1])

        if Obj.int_cov_ratio[-1] > 1:
            val.write("The Company has a GOOD Interest Coverage Ratio\n")
        else:
            val.write("The Company has a BAD Interest Coverage Ratio\n")
        val.write("Interest Coverage Ratio = %f \n\n" % Obj.int_cov_ratio[-1])

        # Liquidity Ratio
        val.write("2) LIQUIDITY RATIO: \n")
        if Obj.cur_ratio[-1] > 2:

            val.write("The Company has a GOOD Current Ratio\n")
        else:
            val.write("The Company has a BAD Current Ratio\n")
        val.write("Current Ratio = %f \n" % Obj.cur_ratio[-1])

        if Obj.cshratio[-1] > 1:
            val.write("The Company has a GOOD Cash Ratio\n")
        else:
            val.write("The Company has a BAD Cash Ratio\n")

        val.write("Cash Ratio = %f \n" % Obj.cshratio[-1])

        if Obj.op_cashflow_ratio[-1] > 1:
            val.write("The Company has a GOOD Operating Cashflow Ratio\n")
        else:
            val.write("The Company has a BAD Operating Cashflow Ratio\n")
        val.write("Operating Cashflow Ratio = %f \n" % Obj.op_cashflow_ratio[-1])

        try:
            if Obj.inv_turnover_ratio[-1] > 5:
                val.write("The Company has a GOOD Inventory Turnover Ratio\n")
            else:
                val.write("The Company has a BAD Inventory Turnover Ratio\n")
            val.write("Inventory Turnover Ratio = %f \n\n" % Obj.inv_turnover_ratio[-1])

        except Exception:
            pass

        # Profitability Ratio
        val.write("3) Profitability RATIO: \n")
        if Obj.opr_income_margin[-1] > 15:
            val.write("The Company has a GOOD Operating Income Margin\n")
        else:
            val.write("The Company has a BAD Operating Income Margin\n")
        val.write("Operating Income Margin = %f \n" % Obj.opr_income_margin[-1])

        if Obj.net_prft_margin[-1] > 15:
            val.write("The Company has a GOOD Net Profit Margin\n")
        else:
            val.write("The Company has a BAD Net Profit Margin\n")
        val.write("Net Profit Margin = %f \n" % Obj.net_prft_margin[-1])

        if Obj.roe[-1] > 10:
            val.write("The Company has a GOOD Return on Equity\n")
        else:
            val.write("The Company has a BAD Return on Equity\n")
        val.write("Return on Equity = %f \n" % Obj.roe[-1])

        if Obj.roa[-1] > 10:
            val.write("The Company has a GOOD Return on Assets\n")
        else:
            val.write("The Company has a BAD Return on Assets\n")
        val.write("Return on Assets = %f \n\n" % Obj.roa[-1])

        if Obj.roce[-1] > 10:
            val.write("The Company has a GOOD Return on Capital Employed\n")
        else:
            val.write("The Company has a BAD Return on Capital Employed\n")
        val.write("Return on Capital Employed = %f \n\n" % Obj.roce[-1])

        # Intrinsic Value Calculation
        val.write("--------------------------------------------------------------------\n")
        val.write("----------------------Intrinsic Value Calculation-------------------\n")
        val.write("--------------------------------------------------------------------\n\n")
        val.write(f"WACC Calculation \n")
        val.write("--------------------------------------------------------------------\n")
        val.write(f"Market Cap = {Obj.marketcap} \n")
        val.write(f"Long Term Debt = {Obj.long_term_debt[-1]} \n")
        val.write(f"Beta = {Obj.beta}\n")
        val.write(f"Risk Free Return = {Obj.risk_free_return}\n")
        val.write(f"Corporate Tax = {Obj.corp_tax}\n")
        val.write("--------------------------------------------------------------------\n")
        val.write(f"Weighted Equity Capital = {Obj.weighted_equity_capital}\n")
        val.write(f"Weighted Debt Capital = {Obj.weight_debt_capital}\n")
        val.write(f"ROR Equity Capital = {Obj.ror_equity_capital}\n")
        val.write(f"ROR Debt Capital = {Obj.ror_debt_capital}\n")
        val.write(f"WACC calculated as = {Obj.WACC} \n\n")

        val.write(f"ROCE is {Obj.roce[-1]} and WACC is {Obj.WACC}\n")
        val.write(f"Interest Expense {Obj.interest_expense[-1]}\n")

        val.write(f"CAGR Total Revenue  = {Obj.cagr_tot_rev_gr}\n")
        val.write(f"Present Value  = {Obj.present_value}\n")
        val.write(f"Discount Factor  = {Obj.discount_factor}\n")
        val.write(f"Total Revenue  = {Obj.tot_revenue}\n")
        val.write(f"Present Terminal Value  = {Obj.today_value}\n")
        val.write(f"Shares Outstanding  = {Obj.sharesoutstanding}\n\n")
        val.write(f"Intrinsic Value  = {Obj.intrinsic_value}\n")
        val.write(f"Margin of Safety  = {Obj.margin_of_safety}\n")
