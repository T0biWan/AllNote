import logging
import sys


class Logger:
     x = {"DEBUG": logging.DEBUG}

    def __init__(self, level):
        LOG_FORMAT = '%(levelname)s:%(funcName)s:%(message)s'
        logging.basicConfig(stream=sys.stdout, level=x["DEBUG"], filemode='w', format=LOG_FORMAT)
        self.logger = logging.getLogger()

    def get_logger(self):
        return self.logger


