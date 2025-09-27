from typing import List
from logging import getLogger, config
from dataclasses import dataclass, fields

import pandas as pd
import numpy as np

from data.inputdata import HotelReviews_Raw 

# 2. Check Data

logger = getLogger('__main__.val')

class Validate_Data:
    def __init__(self, coltype_dict):
        self.coltype_dict : dict = coltype_dict
        self.logger = getLogger('__main__.val.Val')

    def validate_data(self, hotel_reviews) -> pd.DataFrame:
       
        df_hotel_reviews = pd.DataFrame(hotel_reviews)
        df_hotel_reviews = df_hotel_reviews.replace('NA',np.nan)
        df_hotel_reviews = df_hotel_reviews.astype(self.coltype_dict)

        self.logger.info("<<Data Information>>")
        self.logger.info(f"{df_hotel_reviews.info()}")
        self.logger.info("<<Data Describe>>")
        self.logger.info(f"{df_hotel_reviews.describe()}")
        self.logger.info("Complete 2.Check Data")

        return df_hotel_reviews
