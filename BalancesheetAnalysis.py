"""
Author : Bharani Deepak
Info   : This Subclass contains Methods and Attributes for analysing Balance Sheet and
         it inherits from Base Class
Purpose: Accesses the Balance Sheet and performs Balance Sheet analysis
"""
from Base import *
import pandas as pd

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

class BalancesheetAnalysis(Base):

    def __init__(self):
        super().__init__()
        self.G_cur_ratio = self.currentratio()                      # Growth in current ratio

    def currentratio(self):

        logger.info("Calculating Current Ratio and its growth")
        cur_asset = np.array(self.balsheet.loc['Current Assets']).astype('int32')
        cur_liability = np.array(self.balsheet.loc['Current Liabilities']).astype('int32')
        cur_ratio = cur_asset/cur_liability

        return Base.percentage_growth(cur_ratio)
