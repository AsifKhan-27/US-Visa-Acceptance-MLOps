from US_Visa.logger import logging
from US_Visa.exception import USVisaException
import sys
from US_Visa.pipeline.training_pipeline import TrainPipeline

logging.info("Welcome to the custom log")


# try:
#     a = 2/0
# except Exception as e:
#     raise USVisaException(e, sys)


obj = TrainPipeline()
obj.run_pipeline()

logging.info('Finished running demo.py')