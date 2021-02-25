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
        self.G_ebitda_margin = self.ebitda_margin()               # Growth in EBITA Margin


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

    def ebitda_margin(self):

        try:
            """
            EBITDA Margin:
            EBITDA with respect to Total Revenue
            ***HIGHER the BETTER***
            """
            logger.info("Calculating EBITDA Margin")

            self.ebitda = np.array(self.incomestmt.loc['EBITDA']).astype('float')

            print(self.ebitda) 
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
