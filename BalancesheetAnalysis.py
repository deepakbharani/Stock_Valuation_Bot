"""
Author : Bharani Deepak
Info   : This Subclass contains Methods and Attributes for analysing and calculating
         Liquidity Ratios
Helper : Plot arguments (labeltext,xlabel,ylabel,title,array,xaxis = None):
"""

from Base import *
from Plotter import *

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

pt = Plotter()

class LiquidityRatio(Base,Plotter):

    def __init__(self):
        super().__init__()
        self.G_cur_ratio = self.currentratio()                      # Growth in current ratio
        self.G_debtequity = self.debttoequity()                     # Growth in Debt to Equity
        self.G_cashratio = self.cashratio()                         # Growth in Cash Ratio
        self.G_oper_cashflow_ratio = self.oper_cashflow_ratio()     # Growth in Operating Cashflow


    def currentratio(self):

        """
        Current Ratio:
        The ability of a company to pay off its current liabilities
        ***HIGHER the BETTER***
        """

        logger.info("Calculating Current Ratio and its growth")
        self.cur_asset = np.array(self.balsheet.loc['Current Assets']).astype('float')
        self.cur_liability = np.array(self.balsheet.loc['Current Liabilities']).astype('float')
        self.cur_ratio = np.divide(self.cur_asset,self.cur_liability)
        self.A_cur_ratio = self.cur_ratio.mean()

        ## PLOTTING
        # pt.twoDplot('Current Asset / Current Liability', 'Years', 'Current Ratio', 'Current Ratio past few Years', self.cur_ratio,
        #             self.bs_column_name[1:])
        # pt.twoDplot('Growth in Current Ratio', 'Years', 'Growth', 'Current Ratio growth', Base.percentage_growth(self.cur_ratio))

        return Base.percentage_growth(self.cur_ratio)

    def debttoequity(self):

        """
        Debt to Equity ratio:
        Long term debt to its shareholders equity
        ***LOWER the BETTER***
        """
        logger.info("Calculating Debt to Equity ratio")
        self.long_term_debt = np.array(self.balsheet.loc['Long Term Debt']).astype('float')
        self.shareholder_equity = np.array(self.balsheet.loc['Stockholders\' Equity']).astype('float')
        self.debt2equity = np.divide(self.long_term_debt,self.shareholder_equity)

        ## PLOTTING
        # pt.twoDplot('Debt to Equity', 'Years', 'Debt to Equity', 'Debt to Equity ratio', self.debt2equity,
        #             self.bs_column_name[1:])

        return Base.percentage_growth(self.debt2equity)

    def cashratio(self):

        """
        Cash Ratio:
        Cash and Cash Equivalent to Current Liabilities
        ***HIGHER the BETTER***
        """
        logger.info("Calculating Cash Ratio")
        self.cash_cashequ = np.array(self.balsheet.loc['Cash And Cash Equivalents']).astype('float')
        self.curr_liabilities = np.array(self.balsheet.loc['Current Liabilities']).astype('float')
        self.cshratio = np.divide(self.cash_cashequ,self.cur_liability)

        ## PLOTTING
        # pt.twoDplot('Cash and Cash Equivalent to Current Liabilities', 'Years', 'Cash Ratio', 'Cash Ratio', self.cshratio,
        #             self.bs_column_name[1:])

        return Base.percentage_growth(self.cshratio)

    def oper_cashflow_ratio(self):

        """
        Operative Cashflow Ratio:
        The operating cash flow ratio is a measure of how readily current liabilities
        are covered by the cash flows generated from a company's operations.
        ***HIGHER the BETTER***
        """

        logger.info("Calculating Operating Cashflow ratio")
        self.op_cashflow = np.array(self.cashflow.loc['Operating Cash Flow']).astype('float')
        self.op_cashflow_ratio = np.divide(self.op_cashflow[0:-1],self.cur_liability)
        
        ## PLOTTING
        # pt.twoDplot('Operating Cashflow to Current Liabilities', 'Years', 'Operating Cashflow ratio',
        #             'Operating Cashflow ratio', self.op_cashflow_ratio,self.bs_column_name[1:])
        # pt.twoDplot('Growth in Current Ratio', 'Years', 'Growth', 'Current Ratio growth', Base.percentage_growth(self.cur_ratio))

        return Base.percentage_growth(self.op_cashflow_ratio)
