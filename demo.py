# test-1

# from us_visa.logger import logging
# from us_visa.exception import USvisaException
# import sys

# try:
#     r = 3/0
#     print(r)
# except Exception as e:
#     logging.info(e)
#     raise USvisaException(e, sys)

# test-2

# import os

# mongodburl = os.getenv("MONGODB_URL")
# print(mongodburl)

# test-3

from us_visa.pipline.training_pipeline import TrainingPipeline

pipeline = TrainingPipeline()
pipeline.run_pipeline()