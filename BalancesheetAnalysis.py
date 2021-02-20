"""
Author : Bharani Deepak
Info   : This Subclass contains Methods and Attributes for analysing Balance Sheet and
         it inherits from Base Class
Purpose: Accesses the Balance Sheet and performs Balance Sheet analysis
Helper : Plot arguments (labeltext,xlabel,ylabel,title,array,xaxis = None):
"""

from Base import *
from Plotter import *

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

pt = Plotter()

class BalancesheetAnalysis(Base,Plotter):

    def __init__(self):
        super().__init__()
        self.G_cur_ratio = self.currentratio()                      # Growth in current ratio
        self.G_bookval = self.bookvalue()                           # Growth in bookvalue

    def currentratio(self):

        logger.info("Calculating Current Ratio and its growth")
        cur_asset = np.array(self.balsheet.loc['Current Assets']).astype('int32')
        cur_liability = np.array(self.balsheet.loc['Current Liabilities']).astype('int32')
        cur_ratio = np.divide(cur_asset,cur_liability)
        self.A_cur_ratio = cur_ratio.mean()

        # pt.twoDplot('Current Ratio', 'Years', 'Current Ratio', 'Current Ratio past few Years', cur_ratio,
        #             self.bs_column_name[1:])
        # pt.twoDplot('Growth in Current Ratio', 'Years', 'Growth', 'Current Ratio growth', Base.percentage_growth(cur_ratio))

        return Base.percentage_growth(cur_ratio)

    def bookvalue(self):

        logger.info("Analysing Book Value")
        bookval = np.array(self.balsheet.loc['Tangible Book Value']).astype('int32')

        pt.twoDplot('Tangiable Book Value', 'Years', 'Tangiable Book Value', 'Tangiable Book Value', bookval,
                    self.bs_column_name[1:])

        return Base.percentage_growth(bookval)
