"""
Author : Bharani Deepak
Info   : This Subclass contains Methods and Attributes for analysing Balance Sheet and
         it inherits from Base Class
Purpose: Accesses the Balance Sheet and performs Balance Sheet analysis
"""
from Base import *
import pandas as pd

class BalancesheetAnalysis(Base):

    def __init__(self):
        super().__init__()
        self.G_cur_ratio = self.currentratio()

    def currentratio(self):

        logger.info("Calculating Current Ratio and its growth")
        cur_asset = np.array(self.balsheet.loc['Current Assets']).astype('int32')
        cur_liability = np.array(self.balsheet.loc['Current Liabilities']).astype('int32')
        cur_ratio = cur_asset/cur_liability
        
        return Base.percentage_growth(cur_ratio)
