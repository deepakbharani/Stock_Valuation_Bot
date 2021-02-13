"""
Author : Bharani Deepak
Info   : This Base Class contains common Methods and Attributes
Purpose: Reads the financial statements and returns dataframes containing the data
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
            data_bs = bs.readlines()
            data_bs.pop(0)
            self.balsheet = pd.DataFrame(self.listformatter(data_bs))
            logger.info("Balance sheet read")

        with open(self.path[1], 'r') as cf:
            logger.info("Reading Cash flow statement")
            data_cf = cf.readlines()
            data_cf.pop(0)
            self.cashflow = pd.DataFrame(self.listformatter(data_cf))
            logger.info("Cash flow statement read")

        with open(self.path[2], 'r') as ins:
            logger.info("Reading Income statement")
            data_ins = ins.readlines()
            data_ins.pop(0)
            self.incomestmt = pd.DataFrame(self.listformatter(data_ins))
            logger.info("Income statement read")

        return self.balsheet, self.cashflow, self.incomestmt

    def listformatter(self, data):
        # This function formats the data from input file to meaningful elements of the list
        formatted_list = []
        for items in data:
            items = items.split()
            items[0:(len(items) - 4)] = [' '.join(items[0:(len(items) - 4)])]
            formatted_list.append(items)

        return formatted_list


