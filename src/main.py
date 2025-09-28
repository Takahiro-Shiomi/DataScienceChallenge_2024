import sys

import conf

from logging import getLogger, config
import json

from load.load_data import Load_Data
from validation.validate_data import Validate_Data
from preprocess.data_preprocess import Data_Preprocess
from modeling.modeling import Modeling
from export.export_data import Export_Data

with open("/home/ec2-user/DataScienceChallenge_2024/log/log_config.json") as f:
    config.dictConfig(json.load(f))

logger = getLogger('__main__')

def main():

    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")

    # 0.Load Setting
    logger.info("---------- 0. Start Load Setting ----------")
    s3_conf = conf.s3_conf()
    data_conf = conf.data_conf()
    model_conf = conf.model_conf()

    # 1.Load Data
    logger.info("---------- 1. Start Load Data ----------")
    loaddata = Load_Data(s3_conf.s3_buket, s3_conf.input_folder, s3_conf.input_file)
    exportdata = Export_Data(s3_conf.s3_buket, s3_conf.output_folder, s3_conf.output_model)
    hotel_reviews = loaddata.load_data()
    
    # 2.Check Data
    logger.info("---------- 2. Start Check Data ----------")
    validatedata = Validate_Data(data_conf.coltype_dict)
    val_hotel_reviews = validatedata.validate_data(hotel_reviews, profile_flg)

    # 3.Data Preprocessing
    logger.info("---------- 3. Start Data Preprocessing ----------")
    preprocessing = Data_Preprocess()
    df_hotel_reviews = preprocessing.data_preprocessing(val_hotel_reviews)

    # 4.Create Model
    logger.info("---------- 4. Start Create Model ----------")
    modeling = Modeling()
    model = modeling.create_model(df_hotel_reviews)

    # 5.Adapt Model
    logger.info("---------- 5. Start Adapt Model ----------")

    # 6.Export
    logger.info("---------- 6. Start Export file ----------")
    exportdata.export_model(model)


if __name__ == "__main__":

    main()
