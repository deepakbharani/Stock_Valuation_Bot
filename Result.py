"""
Author : Bharani Deepak
Info   : This class writes the valuation results to a file
"""
from dataclasses import dataclass
from DCF import *

logging.basicConfig(filename="logfile.log", level=logging.INFO,
                    format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',
                    datefmt='[%d/%m/%Y] (%H:%M:%S)', filemode='w')

mainlogger = logging.getLogger(__name__)
mainlogger.info("Stock Valuation started")

@dataclass
class Result():
    Obj = DCF()

    # ## Write Results to file
    destination_path = os.path.dirname(__file__)
    destination_path = destination_path.replace('/', '\\')

    destination_path = os.path.join(destination_path, "valuations.txt")

    with open(destination_path, 'w') as val:
        val.write("--------------------------------------------------------------------\n")
        val.write("-----------------------------VALUATION------------------------------\n")
        val.write("--------------------------------------------------------------------\n\n")
        val.write("1) SOLVENCY RATIO: \n")
        if Obj.debt2equity[0] < 1:
            val.write("The Company has a GOOD Debt to Equity ratio\n")
        else:
            val.write("The Company has a BAD Debt to Equity ratio\n")
        val.write("Debt to Equity Ratio = %f \n" % Obj.debt2equity[0])
        val.write("WACC calculated as = %f \n" % Obj.WACC)