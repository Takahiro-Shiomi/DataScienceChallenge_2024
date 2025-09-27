import boto3
import tempfile
import csv
import pickle

from typing import List
from logging import getLogger, config


# 6.Export Data

logger = getLogger("__main__.export")

class Export_Data:
    def __init__(self, s3_bucket, output_folder, output_model):
        self.s3_bucket : str = s3_bucket
        self.output_folder  : str = output_folder
        self.output_model : str = output_model

        self.logger = getLogger("__main__.export.Export")

    def export_model(self, model):
        # Create TemppraryDirectory 
        tmpdir = tempfile.TemporaryDirectory()
        tmp = tmpdir.name + '/'
        tmp_output = tmp + 'tmp_output_model.pkl'

        # Output Model To S3
        s3_client = boto3.client('s3')
        s3 = boto3.resource('s3')
        pickle.dump(model, open(tmp_output, 'wb'))
        s3.Bucket(self.s3_bucket).upload_file(tmp_output,self.output_folder + '/' + self.output_model)
        
        tmpdir.cleanup()
        
        self.logger.info("Complete 6.Export Model")
