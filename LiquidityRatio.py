"""
Author : Bharani Deepak
Info   : This Subclass contains Methods and Attributes for analysing and calculating
         Liquidity Ratios
Helper : Plot arguments (labeltext,xlabel,ylabel,title,array,xaxis = None):
"""

from Base import *
from Plotter import *
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

pt = Plotter()

class LiquidityRatio(Base,Plotter):

    def __init__(self):
        super().__init__()
        self.G_cur_ratio = self.currentratio()                      # Growth in current ratio
        self.G_cashratio = self.cashratio()                         # Growth in Cash ratio
        self.G_oper_cashflow_ratio = self.oper_cashflow_ratio()     # Growth in Operating Cashflow
        self.G_inv_turnover_ratio = self.inventory_turnover_ratio() # Growth in Inventory turnover ratio

        pt.twoDplot("Liquidity Ratio", self.cur_ratio, self.cshratio, self.op_cashflow_ratio, self.inv_turnover_ratio)

    def valuation(func):

        def wrapper(*args,**kwargs):

            if func.__name__ == "currentratio":
                cr = func(*args,*kwargs)
                if cr.mean() > 2:
                    logger.info("Current Ratio is GOOD : %f", cr.mean())
                else:
                    logger.info("Current Ratio is BAD : %f", cr.mean())

            elif func.__name__ == "cashratio":
                cashr = func(*args,**kwargs)
                if cashr.mean() > 1:
                    logger.info("Cash Ratio is GOOD : %f",cashr.mean())
                else:
                    logger.info("Cash Ratio is BAD : %f", cashr.mean())

            elif func.__name__ == "oper_cashflow_ratio":
                ocr = func(*args,**kwargs)
                if ocr.mean() > 1:
                    logger.info("Operating Cashflow Ratio is GOOD : %f",ocr.mean())
                else:
                    logger.info("Operating Cashflow Ratio is BAD : %f", ocr.mean())

            else:
                # decorator code for inventory turnover ratio
                itr = func(*args, **kwargs)
                if itr.mean() > 5:
                    logger.info("Inventory Turnover Ratio is GOOD : %f", itr.mean())
                else:
                    logger.info("Inventory Turnover Ratio is BAD : %f", itr.mean())

        return wrapper

    @valuation
    def currentratio(self):

        try:
            """
            Current Ratio:
            The ability of a company to pay off its current liabilities
            ***HIGHER the BETTER***
            """

            logger.info("Calculating Current Ratio and its growth")
            self.cur_ratio = np.divide(self.cur_assets,self.cur_liabilities)
            self.A_cur_ratio = self.cur_ratio.mean()
            return self.cur_ratio

        except KeyError:
            logger.error("Current Ratio can't be calculated")
            logger.exception(KeyError)

        except ValueError:
            logger.exception(ValueError)

        except AttributeError:
            logger.exception(AttributeError)

    @valuation
    def cashratio(self):

        try:
            """
            Cash Ratio:
            Cash and Cash Equivalent to Current Liabilities
            ***HIGHER the BETTER***
            """
            logger.info("Calculating Cash Ratio")
            self.cshratio = np.divide(self.cash_cashequ,self.cur_liabilities)

            return self.cshratio

        except KeyError:
            logger.error("Cash Ratio can't be calculated")
            logger.exception(KeyError)

        except ValueError:
            logger.exception(ValueError)

        except AttributeError:
            logger.exception(AttributeError)

    @valuation
    def oper_cashflow_ratio(self):

        try:
            """
            Operative Cashflow Ratio:
            The operating cash flow ratio is a measure of how readily current liabilities
            are covered by the cash flows generated from a company's operations.
            ***HIGHER the BETTER***
            """

            logger.info("Calculating Operating Cashflow ratio")
            self.op_cashflow_ratio = np.divide(self.op_cashflow,self.cur_liabilities)
            return self.op_cashflow_ratio

        except Exception:
            logger.error("Operative Cashflow Ratio can't be calculated")
            logger.exception(Exception)
            self.op_cashflow_ratio = [0, 0, 0, 0]

    #@valuation
    def inventory_turnover_ratio(self):

        try:
            """
            Inventory turnover ratio:
            The inventory turnover ratio is a measure of number of times a company has replaced its inventory
            ***HIGHER the BETTER***
            """

            logger.info("Calculating Inventory turnover ratio")
            self.inv_turnover_ratio = np.divide(self.tot_revenue, self.inventory)

            return self.inv_turnover_ratio

        except Exception:
            logger.error("Inventory turnover ratio can't be calculated")
            logger.exception(Exception)
            self.inv_turnover_ratio = [0,0,0,0]