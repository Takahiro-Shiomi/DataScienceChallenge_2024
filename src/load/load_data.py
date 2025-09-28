import boto3
import tempfile
import csv
from typing import List
from logging import getLogger, config

from data.inputdata import HotelReviews_Raw 

# 1.Load Data

logger = getLogger("__main__.load")

class Load_Data:
    def __init__(self, s3_bucket, input_folder, input_file):
        self.s3_bucket : str = s3_bucket
        self.input_folder  : str = input_folder
        self.input_file : str = input_file

        self.logger = getLogger("__main__.load.Load")

    def load_data(self) -> List[HotelReviews_Raw]:
        # Create TemppraryDirectory 
        tmpdir = tempfile.TemporaryDirectory()
        tmp = tmpdir.name + '/'
        tmp_input = tmp + 'tmp_input.csv'

        # Load File From S3
        s3_client = boto3.client('s3')
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(self.s3_bucket)
        bucket.download_file(self.input_folder + '/' + self.input_file, tmp_input)

        # Store Value in DataClass
        hotel_reviews : list = [] 
        with open(tmp_input, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                hotel_review = HotelReviews_Raw(
                                    Hotel_Address=row['Hotel_Address'],
                                    Additional_Number_of_Scoring=row['Additional_Number_of_Scoring'],
                                    Review_Date=row['Review_Date'],
                                    Average_Score=row['Average_Score'],
                                    Hotel_Name=row['Hotel_Name'],
                                    Reviewer_Nationality=row['Reviewer_Nationality'],
                                    Negative_Review=row['Negative_Review'],
                                    Review_Total_Negative_Word_Counts=row['Review_Total_Negative_Word_Counts'],
                                    Total_Number_of_Reviews=row['Total_Number_of_Reviews'],
                                    Positive_Review=row['Positive_Review'],
                                    Review_Total_Positive_Word_Counts=row['Review_Total_Positive_Word_Counts'],
                                    Total_Number_of_Reviews_Reviewer_Has_Given=row['Total_Number_of_Reviews_Reviewer_Has_Given'],
                                    Reviewer_Score=row['Reviewer_Score'],
                                    Tags=row['Tags'],
                                    days_since_review=row['days_since_review'],
                                    lat=row['lat'],
                                    lng=row['lng']
                                    )
                hotel_reviews.append(hotel_review)
        self.logger.info("Data Length = " + str(len(hotel_reviews)))
        
        tmpdir.cleanup()
        
        self.logger.info("Complete 1.Load Data")
        
        return hotel_reviews