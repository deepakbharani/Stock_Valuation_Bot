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
        logger.info("Calculating Current Ratio")
        print(self.balsheet.loc['Current Assets'].dtypes)
        # print(self.balsheet.loc[['Current Assets'],['9/29/2017']])
        # print(self.balsheet.columns)

        # growth = Base.percentage_growth(float(self.balsheet.loc[['Current Assets'],['9/29/2017']]),float(self.balsheet.loc[['Current Assets'],['9/29/2018']]))
        # print(growth)
