import boto3
import tempfile
import csv
from typing import List

from data.inputdata import HotelReviews_Raw 

# 1.Load Data

class Load_Rawdata:
    def __init__(self, s3_bucket, input_folder, input_file):
        self.s3_bucket : str = s3_bucket
        self.input_folder  : str = input_folder
        self.input_file : str = input_file

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
        print(len(hotel_reviews))
        return hotel_reviews

    def connect_s3(self):
        # ダウンロード元バケット名
        bucket_name = 'amazon-sagemaker-799695492243-ap-northeast-1-ec1dee4237a7'
        # アップロード先バケット名（今回はダウンロード先と同じ）
        out_bucket_name = bucket_name
        # バケットにあるファイル名
        file_name = 'test-buket/Hotel_Reviews.csv'
        # アップロード先のフォルダ名
        # 下記の例だとS3にresultフォルダが作成され、そこに出力される
        out_folder_name = 'test-buket/result'

        # 一時保存用ディレクトリの作成
        tmpdir = tempfile.TemporaryDirectory()
        tmp = tmpdir.name + '/'

        # 一時的な入力ファイル名（適当な名前で固定)
        # 固定された名前で一時フォルダにダウンロードされる
        tmp_input = tmp + 'tmp.csv'
        # S3からファイルをダウンロード
        s3_client = boto3.client('s3')
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)
        for object in bucket.objects.all():
            print(object.key)
        bucket.download_file(file_name, tmp_input)
        s3.Bucket(out_bucket_name).upload_file(tmp_input,out_folder_name+'/'+ 'output.csv')

        tmpdir.cleanup()

