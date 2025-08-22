import sys

import conf

from logging import getLogger, config
import json

from load.load_data import Load_Rawdata

with open("/home/ec2-user/DataScienceChallenge_2024/log/log_config.json") as f:
    config.dictConfig(json.load(f))

logger = getLogger(__name__)

def main():

    set_conf = conf.conf()

    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")

    loaddata = Load_Rawdata()
    loaddata.connect_s3()

if __name__ == "__main__":
    main()
