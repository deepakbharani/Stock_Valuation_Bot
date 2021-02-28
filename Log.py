"""
Author : Bharani Deepak
Info   : Class decorator for Logging
"""
import logging
from Base import *
from SolvencyRatio import *

logging.basicConfig(filename='logfile.log', level=logging.INFO,
                            format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',
                            datefmt='[%d/%m/%Y] (%H:%M:%S)', filemode='w')
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

class Log(Base):

    def __init__(self,Ofunc):
        super().__init__()
        self.ofunc = Ofunc

    def __call__(self, *args, **kwargs):

        if self.ofunc.__name__ is "debttoequity":
            logger.info("Calculating Debt to Equity ratio")
        else:
            logger.info("Calculating Nothing")

        return self.ofunc(self,*args,**kwargs)
