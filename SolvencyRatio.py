"""
Author : Bharani Deepak
Info   : This Subclass contains Methods and Attributes for analysing and calculating
         Solvency Ratios
Helper : Plot arguments (labeltext,xlabel,ylabel,title,array,xaxis = None):
"""

from LiquidityRatio import *
from Plotter import *
from matplotlib import pyplot as plt

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

        # fig,(ax1,ax2) = plt.subplots(2)
        # fig.suptitle("Solvency Ratios")
        # ax1.plot([1,2,3,4], self.debt2equity, label="Debt to Equity", color='blue', marker='o')
        # ax1.grid(True)
        # ax1.set_title("Debt to Equity")
        # ax1.set_xlabel("Year")
        # ax1.set_ylabel("Debt to Equity")
        # ax1.legend()
        # ax2.plot([1, 2, 3, 4, 5], self.int_cov_ratio, label="Interest coverage ratio", color='purple', marker='o')
        # ax2.grid(True)
        # ax2.set_title("Interest coverage ratio")
        # ax2.set_xlabel("Year")
        # ax2.set_ylabel("Interest coverage ratio")
        # ax2.legend()
        # plt.show()
        pt.twoDplot("SolvencyRatio",self.debt2equity,self.int_cov_ratio)



    def valuation(func):

        def wrapper(*args, **kwargs):
            if func.__name__ == "debttoequity":
                d2e = func(*args, **kwargs)
                if d2e.mean() < 1:
                    logger.info("Debt to Equity Ratio is GOOD : %f",d2e.mean())
                else:
                    logger.info("Debt to Equity Ratio is BAD : %f",d2e.mean())
            elif func.__name__ == "interest_coverage_ratio":
                icr = func(*args, **kwargs)
                if icr.mean() > 2:
                    logger.info("Interest Coverage Ratio is GOOD : %f",icr.mean())
                else:
                    logger.info("Interest Coverage Ratio is BAD : %f",icr.mean())
            else:
                logger.info("Keep working hard")

        return wrapper

    @valuation
    def debttoequity(self,*args, **kwargs):

        try:
            """
            Debt to Equity ratio:
            Long term debt to its shareholders equity
            ***LOWER the BETTER***
            """
            logger.info("Calculating Debt to Equity ratio")
            self.debt2equity = np.divide(self.long_term_debt,self.shareholder_equity)

            ## PLOTTING
            # pt.twoDplot('Debt to Equity', 'Years', 'Debt to Equity', 'Debt to Equity ratio', self.debt2equity,
            #             self.bs_column_name[1:])

            # return self.debt2equity, Base.percentage_growth(self.debt2equity)
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

            ## PLOTTING
            # pt.twoDplot('Interest Coverage ratio', 'Years', 'Interest coverage ratio', 'Interest coverage ratio',
            #             self.int_cov_ratio,self.ins_column_name[1:])

            return self.int_cov_ratio

        except KeyError:
            logger.error("Interest Coverage ratio can't be calculated")
            logger.exception(KeyError)

        except ValueError:
            logger.exception(ValueError)

        except AttributeError:
            logger.exception(AttributeError)


