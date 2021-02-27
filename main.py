from ProfitabilityRatio import *
from Plotter import *
from Log import *

if __name__ == "__main__":

    logging.basicConfig(filename='logfile.log',level=logging.INFO, format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',
                        datefmt='[%d/%m/%Y] (%H:%M:%S)',filemode='w')
    mainlogger = logging.getLogger(__name__)

    mainlogger.info("Stock Valuation started")

    # Creating object for class LiquidityRatio
    pr = ProfitabilityRatio()
    pt = Plotter()