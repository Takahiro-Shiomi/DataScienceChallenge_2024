from dataclasses import dataclass

@dataclass(frozen=True)
class conf:
    s3_buket : str =  'amazon-sagemaker-799695492243-ap-northeast-1-ec1dee4237a7'
    input_folder : str = 'test-buket'
    input_file : str = 'Hotel_Reviews.csv'
    output_folder : str = 'test-buket/result'
    output_file : str = 'output.csv'
