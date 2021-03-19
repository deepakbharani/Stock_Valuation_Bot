"""
Author : Bharani Deepak
Info   : This Base Class contains common Methods and Attributes
Purpose: Reads the financial statements and returns dataframes containing the data
"""

import os
import logging
import pandas as pd
import numpy as np
import yfinance.yfinance as yf

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

class Base:

    def __init__(self,path = None):

        self.get_financials()

        # files inside "input" folder is defined in tuple
        self.indata = ('balance_sheet.txt', 'cash_flow.txt', 'income_statement.txt')

        if path == None:
            self.path = []
        else:
            self.path = path

        if len(self.indata) is 3:
            logger.info("All 3 Financial statements have been accepted")
            self.balsheet,self.cashflow,self.incomestmt = self.readfinancials()
            self.variablefunction()
        else:
            logger.error("There must be 3 financial statements -> please check input folder")

    def setup_logger(self,name,log_file):

        file_handler = logging.FileHandler(log_file)
        logger = logging.getLogger(name)
        logger.setLevel(logging.ERROR)
        logger.addHandler(file_handler)

        return logger

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

    def variablefunction(self):

        # Balance Sheet parameters
        self.tot_assets = np.array(self.balsheet.loc['Total Assets']).astype('float')
        self.cur_assets = np.array(self.balsheet.loc['Current Assets']).astype('float')
        self.cash_cashequ = np.array(self.balsheet.loc['Cash And Cash Equivalents']).astype('float')
        self.inventory = np.array(self.balsheet.loc['Inventory']).astype('float')
        self.tot_noncur_assets = np.array(self.balsheet.loc['Total non-current assets']).astype('float')
        self.cur_liabilities = np.array(self.balsheet.loc['Current Liabilities']).astype('float')
        self.shareholder_equity = np.array(self.balsheet.loc['Stockholders\' Equity']).astype('float')
        self.long_term_debt = np.array(self.balsheet.loc['Long Term Debt']).astype('float')

        # Cashflow statement parameters
        self.op_cashflow = np.array(self.cashflow.loc['Operating Cash Flow']).astype('float')
        self.free_cashflow = np.array(self.cashflow.loc['Free Cash Flow']).astype('float')

        # Income statement parameters
        self.tot_revenue = np.array(self.incomestmt.loc['Total Revenue']).astype('float')
        self.ebit = np.array(self.incomestmt.loc['EBIT']).astype('float')
        self.interest_expense = np.array(self.incomestmt.loc['Interest Expense']).astype('float')
        self.opr_income = np.array(self.incomestmt.loc['Operating Income']).astype('float')
        self.net_income = np.array(self.incomestmt.loc['Net Income']).astype('float')
        self.ebitda = np.array(self.incomestmt.loc['EBITDA']).astype('float')

    def get_financials(self):
        self.stock_ticker = 'AAPL'
        self.tic = yf.Ticker(self.stock_ticker)

        # Cashflow statement parameters
        self.op_cashflow = np.array(self.tic.cashflow.loc['Total Cash From Operating Activities'])
        self.interest_expense = np.array(self.tic.financials.loc['Interest Expense'])
        self.tax_expense = np.array(self.tic.financials.loc['Income Tax Expense'])
        self.capex = np.array(self.tic.cashflow.loc['Capital Expenditures'])
        self.free_cashflow = self.op_cashflow+self.interest_expense-self.tax_expense-self.capex

        print("Op Cashflow", self.op_cashflow)
        print("free Cashflow", self.free_cashflow)



    @classmethod
    def percentage_growth(self,vector):

        # Calculate percentage change / growth for two value
        growth = []
        for i in range(0,len(vector)-1):
            growth.append(((vector[i+1]-vector[i])/vector[i]) * 100)

        return growth