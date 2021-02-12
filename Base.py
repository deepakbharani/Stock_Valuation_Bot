"""
Author : Bharani Deepak
Info   : This Base Class contains common Methods and Attributes
Purpose: Reads the financial statements and returns lists containing the data
"""
import os
import logging
import pandas as pd

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

class Base:

    def __init__(self,path=[]):

        # files inside "input" folder is defined in tuple
        self.indata = ('balance_sheet.txt', 'cash_flow.txt', 'income_statement.txt')
        self.path = path

        if len(self.indata) is 3:
            logger.info("All 3 Financial statements have been accepted")
            self.balsheet,self.cashflow,self.incomestmt = self.readfinancials()
        else:
            logger.error("There must be 3 financial statements -> please check input folder")

    def readfinancials(self):

        # source_path is the path where this script is saved
        self.source_path = os.path.dirname(__file__)
        self.source_path = self.source_path.replace('/', '\\')

        logger.info("Creating list of paths for the files containing financial data")
        # Set path for all the financial files inside "inputs" folder
        for file in self.indata:
            self.path.append(os.path.join(self.source_path, 'inputs\\', file))

        with open(self.path[0], 'r') as bs:
            logger.info("Reading Balance sheet")
            self.balsheet = bs.readlines()
            #self.balsheet = pd.read_table(self.path[0])
            self.balsheet = pd.DataFrame(self.balsheet)
            self.balsheet = self.balsheet.drop(self.balsheet.index[0])
            self.balsheet = self.balsheet.apply(lambda x: pd.Series(str(x).split("\\t")))
            logger.info("Balance sheet read")

        with open(self.path[1], 'r') as cf:
            logger.info("Reading Cash flow statement")
            self.cashflow = cf.readlines()
            self.cashflow = [i.split() for i in self.cashflow]
            logger.info("Cash flow statement read")

        with open(self.path[1], 'r') as ins:
            logger.info("Reading Income statement")
            self.incomestmt = ins.readlines()
            self.incomestmt = [i.split() for i in self.incomestmt]
            logger.info("Income statement read")

        return self.balsheet,self.cashflow, self.incomestmt
