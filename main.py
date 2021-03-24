from DCF import *
import yfinance.yfinance as yf
from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":

    logging.basicConfig(filename="logfile.log", level=logging.INFO,
                        format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',
                        datefmt='[%d/%m/%Y] (%H:%M:%S)', filemode='w')

    mainlogger = logging.getLogger(__name__)
    mainlogger.info("Stock Valuation started")

    # Creating object for class DCF
    Obj = DCF()