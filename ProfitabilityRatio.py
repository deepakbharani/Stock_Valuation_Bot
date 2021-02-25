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


    def return_on_asset(self):

        try:
            """
            Return on Asset:
            Ability to produce profits from a company's hard asset
            ***HIGHER the BETTER***
            """
            logger.info("Calculating Return on Assets (ROA)")

            self.net_income = np.array(self.incomestmt.loc['Net Income']).astype('float')
            self.tot_asset = np.array(self.balsheet.loc['Total Assets']).astype('float')
            self.roa = np.divide(self.net_income[:-1],self.tot_asset) * 100

            ## PLOTTING
            # pt.twoDplot('Return on Assets', 'Years', 'Return on Assets', 'ROA',
            #             self.roa,self.bs_column_name[1:])

            return Base.percentage_growth(self.roa)

        except KeyError:
            logger.error("Return on Assets cannot be calculated")
            logger.exception(KeyError)

        except ValueError:
            logger.exception(ValueError)

        except AttributeError:
            logger.exception(AttributeError)

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

            return Base.percentage_growth(self.roe)

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

            self.ebitda = np.array(self.incomestmt.loc['EBITDA']).astype('float')
            self.tot_revenue = np.array(self.incomestmt.loc['Total Revenue']).astype('float')
            self.ebitda_margin = np.divide(self.ebitda,self.tot_revenue) * 100

            ## PLOTTING
            # pt.twoDplot('EBITDA Margin', 'Years', 'EBITDA Margin', 'EBITDA Margin',
            #             self.ebitda_margin,self.ins_column_name[1:])

            return # Base.percentage_growth(self.ebitda_margin)

        except KeyError:
            logger.error("EBITDA Margin cannot be calculated")
            logger.exception(KeyError)

        except ValueError:
            logger.exception(ValueError)

        except AttributeError:
            logger.exception(AttributeError)

    def net_profit_margin(self):

        try:
            """
            Net Profit Margin:
            Net income with respect to Total Revenue
            ***HIGHER the BETTER***
            """
            logger.info("Calculating Net Profit Margin")

            self.net_income = np.array(self.incomestmt.loc['Net Income']).astype('float')
            self.net_prft_margin = np.divide(self.net_income,self.tot_revenue) * 100

            ## PLOTTING
            # pt.twoDplot('Net Profit Margin', 'Years', 'Net Profit Margin', 'Net Profit Margin',
            #             self.net_prft_margin,self.ins_column_name[1:])

            return Base.percentage_growth(self.net_prft_margin)

        except KeyError:
            logger.error("Net Profit Margin cannot be calculated")
            logger.exception(KeyError)

        except ValueError:
            logger.exception(ValueError)

        except AttributeError:
            logger.exception(AttributeError)

    def operating_margin(self):

        try:
            """
            Operating Margin:
            Operating Income with respect to Total Revenue
            ***HIGHER the BETTER***
            """
            logger.info("Calculating Operating Income Margin")

            self.opr_income = np.array(self.incomestmt.loc['Operating Income']).astype('float')
            self.opr_income_margin = np.divide(self.opr_income,self.tot_revenue) * 100

            ## PLOTTING
            # pt.twoDplot('Operating Income Margin', 'Years', 'Operating Income Margin', 'Operating Income Margin',
            #             self.opr_income_margin,self.ins_column_name[1:])

            return Base.percentage_growth(self.opr_income_margin)

        except KeyError:
            logger.error("Operating Income Margin cannot be calculated")
            logger.exception(KeyError)

        except ValueError:
            logger.exception(ValueError)

        except AttributeError:
            logger.exception(AttributeError)