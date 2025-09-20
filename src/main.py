import sys

import conf

from logging import getLogger, config
import json

from load.load_data import Load_Rawdata

with open("/home/ec2-user/DataScienceChallenge_2024/log/log_config.json") as f:
    config.dictConfig(json.load(f))

logger = getLogger(__name__)

def main():

    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")

    # 0.Load Setting
    set_conf = conf.conf()

    # 1.Load Data
    loaddata = Load_Rawdata(set_conf.s3_buket, set_conf.input_folder, set_conf.input_file)
    hotel_review = loaddata.load_data()
    # 2.Check Data

    # 3.Data Preprocessing

    # 4.Create Model

    # 5.Evaluate Model

    # 6.Output Model



if __name__ == "__main__":
    main()
