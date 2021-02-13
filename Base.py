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
            self.balsheet = pd.DataFrame(self.listformatter(data_bs))
            logger.info("Balance sheet read")

        with open(self.path[1], 'r') as cf:
            logger.info("Reading Cash flow statement")
            data_cf = cf.readlines()
            self.cashflow = pd.DataFrame(self.listformatter(data_cf))
            logger.info("Cash flow statement read")

        with open(self.path[2], 'r') as ins:
            logger.info("Reading Income statement")
            data_ins = ins.readlines()
            self.incomestmt = pd.DataFrame(self.listformatter(data_ins))
            logger.info("Income statement read")

        return self.balsheet, self.cashflow, self.incomestmt

    def listformatter(self, data):

        # This function formats the data from input file to meaningful elements of the list
        formatted_list = []
        if len(data[0]) is 46:
            data[0] = "Breakdown 9/29/2020 9/29/2019 9/29/2018 9/29/2017"
            num_years = 4
        elif len(data[0]) is 49:
            data[0] = "Breakdown TTM 9/29/2020 9/29/2019 9/29/2018 9/29/2017"
            num_years = 5
        else:
            num_years = 4

        for items in data:
            items = items.split()
            items[0:(len(items) - num_years)] = [' '.join(items[0:(len(items) - num_years)])]
            formatted_list.append(items)
            
        return formatted_list
