"""
Author : Bharani Deepak
Info   : This Subclass contains Methods and Attributes for analysing and calculating
         Solvency Ratios
Helper : Plot arguments (labeltext,xlabel,ylabel,title,array,xaxis = None):
"""

from LiquidityRatio import *
from Plotter import *

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

pt = Plotter()

class SolvencyRatio(LiquidityRatio,Plotter):

    def __init__(self):
        super().__init__()
        self.G_debtequity = self.debttoequity()                     # Growth in Debt to Equity
        self.G_int_cov_ratio = self.interest_coverage_ratio()       # Growth in interest coverage ratio

    def debttoequity(self):

        try:
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

        except KeyError:
            logger.error("Debt to Equity ratio can't be calculated")
            logger.exception(KeyError)

        except ValueError:
            logger.exception(ValueError)

    def interest_coverage_ratio(self):

        try:
            """
            Interest Coverage ratio:
            The interest coverage ratio measures how many times a 
            company can cover its current interest payment with its available earnings
            ***HIGHER the BETTER***
            """
            logger.info("Calculating Interest Coverage ratio")

            self.ebit = np.array(self.incomestmt.loc['EBIT']).astype('float')
            self.interest_expense = np.array(self.incomestmt.loc['Interest Expense']).astype('float')
            self.int_cov_ratio = np.divide(self.ebit,self.interest_expense)

            ## PLOTTING
            # pt.twoDplot('Interest Coverage ratio', 'Years', 'Interest coverage ratio', 'Interest coverage ratio',
            #             self.int_cov_ratio,self.ins_column_name[1:])

            return Base.percentage_growth(self.int_cov_ratio)

        except KeyError:
            logger.error("Interest Coverage ratio can't be calculated")
            logger.exception(KeyError)

        except ValueError:
            logger.exception(ValueError)
