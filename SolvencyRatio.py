"""
Author : Bharani Deepak
Info   : This Subclass contains Methods and Attributes for analysing and calculating
         Solvency Ratios
Helper : Plot arguments (labeltext,xlabel,ylabel,title,array,xaxis = None):
"""

from LiquidityRatio import *
from Plotter import *
import concurrent.futures

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

        # Call plotter to plot the results
        pt.twoDplot("SolvencyRatio",self.debt2equity,self.int_cov_ratio)

    def valuation(func):

        def wrapper(*args, **kwargs):
            if func.__name__ == "debttoequity":
                d2e = func(*args, **kwargs)
                logger.info("Debt to Equity Ratio is GOOD : %f", d2e.mean()) if d2e.mean()<1 else logger.info("Debt to Equity Ratio is BAD : %f",d2e.mean())
            elif func.__name__ == "interest_coverage_ratio":
                icr = func(*args, **kwargs)
                logger.info("Interest Coverage Ratio is GOOD : %f", icr.mean()) if icr.mean() > 2 else logger.info("Interest Coverage Ratio is BAD : %f",icr.mean())
        return wrapper

    #@valuation
    def debttoequity(self,*args, **kwargs):

        try:
            """
            Debt to Equity ratio:
            Long term debt to its shareholders equity
            ***LOWER the BETTER***
            """
            logger.info("Calculating Debt to Equity ratio")
            self.debt2equity = np.divide(self.long_term_debt,self.shareholder_equity)
            return self.debt2equity

        except KeyError:
            logger.error("Debt to Equity ratio can't be calculated")
            logger.exception(KeyError)

        except ValueError:
            logger.exception(ValueError)

        except AttributeError:
            logger.exception(AttributeError)

    @valuation
    def interest_coverage_ratio(self):

        try:
            """
            Interest Coverage ratio:
            The interest coverage ratio measures how many times a
            company can cover its current interest payment with its available earnings
            ***HIGHER the BETTER***
            """
            logger.info("Calculating Interest Coverage ratio")

            self.int_cov_ratio = np.divide(self.ebit,self.interest_expense)

            return self.int_cov_ratio

        except KeyError:
            logger.error("Interest Coverage ratio can't be calculated")
            logger.exception(KeyError)

        except ValueError:
            logger.exception(ValueError)

        except AttributeError:
            logger.exception(AttributeError)


