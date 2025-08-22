import boto3
import tempfile

class Load_Rawdata:
    def __init__(self):
        self.a = 0

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
        # tmp_input = '/home/ec2-user/DataScienceChallenge_2024/src/data/tmp.csv'
        print(tmp_input)
        # S3からファイルをダウンロード
        s3_client = boto3.client('s3')
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)
        for object in bucket.objects.all():
            print(object.key)
        bucket.download_file(file_name, tmp_input)
        print("a")
        s3.Bucket(out_bucket_name).upload_file(tmp_input,out_folder_name+'/'+ 'output.csv')

        tmpdir.cleanup()

