import sys

import conf

from logging import getLogger, config
import json

from load.load_data import Load_Rawdata
from load.validate_data import Validate_Data
from preprocess.data_preprocess import Data_Preprocess
from modeling.modeling import Modeling

with open("/home/ec2-user/DataScienceChallenge_2024/log/log_config.json") as f:
    config.dictConfig(json.load(f))

logger = getLogger('__main__')

def main():

    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")

    # 0.Load Setting
    set_conf = conf.conf()

    # 1.Load Data
    loaddata = Load_Rawdata(set_conf.s3_buket, set_conf.input_folder, set_conf.input_file)
    hotel_reviews = loaddata.load_data()
    
    # 2.Check Data
    validatedata = Validate_Data()
    val_hotel_reviews = validatedata.validate_data(hotel_reviews)

    # 3.Data Preprocessing
    preprocessing = Data_Preprocess()
    df_hotel_reviews = preprocessing.data_preprocessing(val_hotel_reviews)

    # 4.Create Model
    modeling = Modeling()
    model = modeling.create_model(df_hotel_reviews)

    # 5.Evaluate Model

    # 6.Output Model



if __name__ == "__main__":
    main()
