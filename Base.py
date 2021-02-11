"""
Author : Bharani Deepak
Info   : This Base Class contains common Methods and Attributes
Purpose: Reads the financial statements and returns tuples containing the data
"""
import os
import logging

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
            self.balsheet = tuple(bs.readlines())
            logger.info("Balance sheet read")

        with open(self.path[1], 'r') as cf:
            logger.info("Reading Cash flow statement")
            self.cashflow = tuple(cf.readlines())
            logger.info("Cash flow statement read")

        with open(self.path[1], 'r') as ins:
            logger.info("Reading Income statement")
            self.incomestmt = tuple(ins.readlines())
            logger.info("Income statement read")

        return self.balsheet, self.cashflow, self.incomestmt
