from US_Visa.logger import logging
from US_Visa.exception import USVisaException
import sys

logging.info("Welcome to the custom log")


try:
    a = 2/0
except Exception as e:
    raise USVisaException(e, sys)    