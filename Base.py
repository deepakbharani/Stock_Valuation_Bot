"""
Author: Bharani Deepak
Info  : This Base Class contains common Methods and Attributes
"""
import os
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

class Base:

    def __init__(self,input_data=[],path=[]):
        self.indata = input_data
        self.path = path

        if len(self.indata) is 3:
            logger.info("All 3 Financial statements have been accepted")
            self.readfinancials()
        else:
            logger.error("There must be 3 financial statements -> please check input folder")

    def readfinancials(self):

        # source_path is the path where this script is saved
        source_path = os.path.dirname(__file__)
        source_path = source_path.replace('/', '\\')

        logger.info("Creating list of paths for the files containing financial data")
        # Set path for all the financial files inside "inputs" folder
        for file in self.indata:
            self.path.append(os.path.join(source_path, 'inputs\\', file))

        with open(self.path[0], 'r') as bs:
            balsheet = bs.readlines()

        with open(self.path[1], 'r') as cf:
            cashflow = cf.readlines()

        with open(self.path[1], 'r') as ins:
            incomestmt = ins.readlines()

        return balsheet, cashflow,incomestmt
