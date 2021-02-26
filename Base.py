"""
Author : Bharani Deepak
Info   : This Base Class contains common Methods and Attributes
Purpose: Reads the financial statements and returns dataframes containing the data
"""

import os
import logging
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

class Base:

    def __init__(self,path = None):

        # files inside "input" folder is defined in tuple
        self.indata = ('balance_sheet.txt', 'cash_flow.txt', 'income_statement.txt')

        if path == None:
            self.path = []
        else:
            self.path = path


        if len(self.indata) is 3:
            logger.info("All 3 Financial statements have been accepted")
            self.balsheet,self.cashflow,self.incomestmt = self.readfinancials()
        else:
            logger.error("There must be 3 financial statements -> please check input folder")



        # def logger():
        #
        #     def log():
        #
        #
        #     return log



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
            self.balsheet,self.bs_column_name = self.listformatter(data_bs)
            logger.info("Balance sheet read")

        with open(self.path[1], 'r') as cf:
            logger.info("Reading Cash flow statement")
            data_cf = cf.readlines()
            self.cashflow,self.cs_column_name = self.listformatter(data_cf)
            logger.info("Cash flow statement read")

        with open(self.path[2], 'r') as ins:
            logger.info("Reading Income statement")
            data_ins = ins.readlines()
            self.incomestmt,self.ins_column_name = self.listformatter(data_ins)
            logger.info("Income statement read")

        return self.balsheet, self.cashflow, self.incomestmt

    def listformatter(self, data):

        # This function formats the data from input file to meaningful elements of the list
        formatted_list = []

        if len(data[0]) is 46:
            data[0] = "Breakdown 9/29/2020 9/29/2019 9/29/2018 9/29/2017"
            column_name = list(data[0].split())
            # Rearrange columns names for exchanging columns
            cname = column_name.copy()
            cname[1:len(cname)] = cname[1:len(cname)][::-1]
            num_years = 4

        elif len(data[0]) is 49:
            data[0] = "Breakdown TTM 9/29/2020 9/29/2019 9/29/2018 9/29/2017"
            column_name = list(data[0].split())
            # Rearrange columns names for exchanging columns
            cname = column_name.copy()
            cname[1:len(cname)] = cname[1:len(cname)][::-1]
            num_years = 5

        else:
            num_years = 4
            column_name = ['Breakdown','2020','2019','2018','2017']
            # Rearrange columns names for exchanging columns
            cname = column_name.copy()
            cname[1:len(cname)] = cname[1:len(cname)][::-1]

        for items in data:
            items = items.split()
            items[0:(len(items) - num_years)] = [' '.join(items[0:(len(items) - num_years)])]
            for elements in range(-num_years,0):
                items[elements] = items[elements].replace(',', '')
                items[elements] = items[elements].replace('-', '0')
            formatted_list.append(items)

        dataframe = pd.DataFrame(formatted_list, columns = column_name)
        dataframe.drop(0,inplace = True)
        dataframe.set_index('Breakdown',inplace=True)
        dataframe = dataframe[cname[1:len(cname)]]                      # Rearranging columns

        return dataframe,cname

    @classmethod
    def percentage_growth(self,vector):

        # Calculate percentage change / growth for two value
        growth = []
        for i in range(0,len(vector)-1):
            growth.append(((vector[i+1]-vector[i])/vector[i]) * 100)

        return growth
