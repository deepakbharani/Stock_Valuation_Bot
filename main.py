import logging
from Base import *


if __name__ == "__main__":

    logging.basicConfig(filename='logfile.log',level=logging.INFO, format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',
                        datefmt='[%d/%m/%Y] (%H:%M:%S)',filemode='w')
    mainlogger = logging.getLogger(__name__)

    mainlogger.info("Stock Valuation started")

    # files inside "input" folder is defined in tuple
    input_data = ('balance_sheet.txt', 'cash_flow.txt', 'income_statement.txt')

    rf = Base(input_data)


