"""
Author : Bharani Deepak
Info   : Class decorator for Logging
"""
import logging

logging.basicConfig(filename='logfile.log', level=logging.INFO,
                            format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',
                            datefmt='[%d/%m/%Y] (%H:%M:%S)', filemode='w')
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

class Log(object):

    def __init__(self,Ofunc):
        self.ofunc = Ofunc

    def __call__(self, *args, **kwargs):
        logger.info(msg)
        return self.ofunc()
