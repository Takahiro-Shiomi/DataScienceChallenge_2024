from typing import List
from logging import getLogger, config

from data.inputdata import HotelReviews_Raw 

# 2. Check Data

logger = getLogger('__main__.val')

class Validate_Data:
    def __init__(self):
        self.logger = getLogger('__main__.val.Val')

    def validate_data(self, hotel_reviews) -> List[HotelReviews_Raw]:
       
        val_hotel_reviews = hotel_reviews

        self.logger.info("Complete 2.Check Data")

        return val_hotel_reviews
