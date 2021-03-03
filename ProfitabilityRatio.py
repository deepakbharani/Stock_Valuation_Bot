"""
Author : Bharani Deepak
Info   : This Subclass contains Methods and Attributes for analysing and calculating
         Profitability Ratios
Helper : Plot arguments (labeltext,xlabel,ylabel,title,array,xaxis = None):
"""

from SolvencyRatio import *
from Plotter import *

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

pt = Plotter()

class ProfitabilityRatio(SolvencyRatio,Plotter):

    def __init__(self):
        super().__init__()
        self.G_roa = self.return_on_asset()                     # Growth in Return on Assets
        self.G_roe = self.return_on_equity()                    # Growth in Return on Assets
        self.G_ebitda_margin = self.ebitda_margin()             # Growth in EBITA Margin
        self.G_net_profit_margin = self.net_profit_margin()     # Growth in Net Profit Margin
        self.G_opr_income_margin = self.operating_margin()      # Growth in Operating Income Margin

    def valuation(func):

        def wrapper(*args,**kwargs):

            if func.__name__ == "return_on_asset":
                roa = func(*args,*kwargs)
                if roa.mean() >= 10:
                    logger.info("Return on Assets is GOOD : %f",roa.mean())
                else:
                    logger.info("Return on Assets is BAD : %f", roa.mean())

            elif func.__name__ == "return_on_equity":
                roe = func(*args,*kwargs)
                if roe.mean() >= 10:
                    logger.info("Return on Equity is GOOD : %f",roe.mean())
                else:
                    logger.info("Return on Equity is BAD : %f", roe.mean())

            elif func.__name__ == "net_profit_margin":
                npm = func(*args,*kwargs)
                if npm.mean() >= 10:
                    logger.info("Net Profit Margin is GOOD : %f",npm.mean())
                else:
                    logger.info("Net Profit Margin is BAD : %f", npm.mean())

            else:
                # decorator for operating margin
                om = func(*args, *kwargs)
                if om.mean() >= 10:
                    logger.info("Operating Margin is GOOD : %f", om.mean())
                else:
                    logger.info("Operating Margin is BAD : %f", om.mean())

        return wrapper

    @valuation
    def return_on_asset(self):

        try:
            """
            Return on Asset:
            Ability to produce profits from a company's hard asset
            ***HIGHER the BETTER***
            """
            logger.info("Calculating Return on Assets (ROA)")

            self.roa = np.divide(self.net_income[:-1],self.tot_assets) * 100

            ## PLOTTING
            # pt.twoDplot('Return on Assets', 'Years', 'Return on Assets', 'ROA',
            #             self.roa,self.bs_column_name[1:])

            return self.roa

        except KeyError:
            logger.error("Return on Assets cannot be calculated")
            logger.exception(KeyError)

        except ValueError:
            logger.exception(ValueError)

        except AttributeError:
            logger.exception(AttributeError)

    @valuation
    def return_on_equity(self):

        try:
            """
            Return on Equity:
            Ability to make profits from a company's equity
            ***HIGHER the BETTER***
            """
            logger.info("Calculating Return on Equity (ROE)")
            self.roe = np.divide(self.net_income[:-1],self.shareholder_equity) * 100

            ## PLOTTING
            # pt.twoDplot('Return on Equity', 'Years', 'Return on Equity', 'ROE',
            #             self.roe,self.bs_column_name[1:])

            return self.roe

        except KeyError:
            logger.error("Return on Equity cannot be calculated")
            logger.exception(KeyError)

        except ValueError:
            logger.exception(ValueError)

        except AttributeError:
            logger.exception(AttributeError)

    def ebitda_margin(self):

        try:
            """
            EBITDA Margin:
            EBITDA with respect to Total Revenue
            ***HIGHER the BETTER***
            """
            logger.info("Calculating EBITDA Margin")

            self.ebitda_margin = np.divide(self.ebitda,self.tot_revenue) * 100
            logger.info("EBITDA Margin is : %f",self.ebitda_margin.mean())

            ## PLOTTING
            # pt.twoDplot('EBITDA Margin', 'Years', 'EBITDA Margin', 'EBITDA Margin',
            #             self.ebitda_margin,self.ins_column_name[1:])

            return self.ebitda_margin

        except KeyError:
            logger.error("EBITDA Margin cannot be calculated")
            logger.exception(KeyError)

        except ValueError:
            logger.exception(ValueError)

        except AttributeError:
            logger.exception(AttributeError)

    @valuation
    def net_profit_margin(self):

        try:
            """
            Net Profit Margin:
            Net income with respect to Total Revenue
            ***HIGHER the BETTER***
            """
            logger.info("Calculating Net Profit Margin")

            self.net_prft_margin = np.divide(self.net_income,self.tot_revenue) * 100

            ## PLOTTING
            # pt.twoDplot('Net Profit Margin', 'Years', 'Net Profit Margin', 'Net Profit Margin',
            #             self.net_prft_margin,self.ins_column_name[1:])

            return self.net_prft_margin

        except KeyError:
            logger.error("Net Profit Margin cannot be calculated")
            logger.exception(KeyError)

        except ValueError:
            logger.exception(ValueError)

        except AttributeError:
            logger.exception(AttributeError)

    @valuation
    def operating_margin(self):

        try:
            """
            Operating Margin:
            Operating Income with respect to Total Revenue
            ***HIGHER the BETTER***
            """
            logger.info("Calculating Operating Income Margin")

            self.opr_income_margin = np.divide(self.opr_income,self.tot_revenue) * 100

            ## PLOTTING
            # pt.twoDplot('Operating Income Margin', 'Years', 'Operating Income Margin', 'Operating Income Margin',
            #             self.opr_income_margin,self.ins_column_name[1:])

            return self.opr_income_margin

        except KeyError:
            logger.error("Operating Income Margin cannot be calculated")
            logger.exception(KeyError)

        except ValueError:
            logger.exception(ValueError)

        except AttributeError:
            logger.exception(AttributeError)