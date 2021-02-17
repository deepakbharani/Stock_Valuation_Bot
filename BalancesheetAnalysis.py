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

    def currentratio(self):
        logger.info("Calculating Current Ratio and its growth")
        cur_asset = list(map(float, (self.balsheet.loc['Current Assets'])))
        cur_liability = list(map(float, (self.balsheet.loc['Current Liabilities'])))
        cur_ratio = []
        for i in range(0,len(cur_asset)):
            cur_ratio.append(cur_asset[i]/cur_liability[i])

        G_CurrRatio = Base.percentage_growth(cur_ratio)
        print(G_CurrRatio)
