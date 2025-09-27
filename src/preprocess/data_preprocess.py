from typing import List
from logging import getLogger, config

import pandas as pd

from data.inputdata import HotelReviews_Raw 

# 3. Data Preprocessing

logger = getLogger('__main__.preprocess')

class Data_Preprocess:
    def __init__(self):
        self.logger = getLogger('__main__.preprocess.Proprocess')

    def data_preprocessing(self, val_hotel_reviews) -> pd.DataFrame:
       
        df_hotel_reviews = val_hotel_reviews
 
        cols: list =['Average_Score',
                     'Review_Total_Negative_Word_Counts',
                     'Review_Total_Positive_Word_Counts',
                     'Reviewer_Score'
                     ]
        
        df_hotel_reviews = df_hotel_reviews[cols]

        self.logger.info("Complete 3. Data Preprocessing")

        return df_hotel_reviews
