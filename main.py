import logging
import pandas as pd
from Base import *


if __name__ == "__main__":

    logging.basicConfig(filename='logfile.log',level=logging.INFO, format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',
                        datefmt='[%d/%m/%Y] (%H:%M:%S)',filemode='w')
    mainlogger = logging.getLogger(__name__)

    mainlogger.info("Stock Valuation started")

    # Creating object for base class
    baseobj = Base()

    print(baseobj.balsheet)
    df = pd.DataFrame(baseobj.balsheet)

    for items in baseobj.balsheet:
        print(items)
        #items = items.split('\\t')

