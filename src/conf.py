from dataclasses import dataclass, field

@dataclass(frozen=True)
class s3_conf:
    s3_buket : str =  'amazon-sagemaker-799695492243-ap-northeast-1-ec1dee4237a7'
    
    input_folder : str = 'test-buket'
    input_file : str = 'Hotel_Reviews.csv'

    output_folder : str = 'test-buket/result'
    output_file : str = 'output.csv'
    output_model : str = 'output_model.pkl'

@dataclass(frozen=True)
class data_conf:
    col_name :list = field(default_factory=lambda:
                           ['Hotel_Address',
                            'Additional_Number_of_Scoring',
                            'Review_Date',
                            'Average_Score',
                            'Hotel_Name',
                            'Reviewer_Nationality',
                            'Negative_Review',
                            'Review_Total_Negative_Word_Counts',
                            'Total_Number_of_Reviews',
                            'Positive_Review',
                            'Review_Total_Positive_Word_Counts',
                            'Total_Number_of_Reviews_Reviewer_Has_Given',
                            'Reviewer_Score',
                            'Tags',
                            'days_since_review',
                            'lat',
                            'lng'])
    col_type :list = field(default_factory=lambda:
                           ['str',
                            'int',
                            'str',
                            'float',
                            'str',
                            'str',
                            'str',
                            'int',
                            'int',
                            'str',
                            'int',
                            'int',
                            'float',
                            'str',
                            'str',
                            'float',
                            'float'])
    coltype_dict :dict = field(default_factory=lambda:
                         {'Hotel_Address'                : 'str',
                          'Additional_Number_of_Scoring' : 'int',
                          'Review_Date'                  : 'str',
                          'Average_Score'                : 'float',
                          'Hotel_Name'                   : 'str',
                          'Reviewer_Nationality'         : 'str',
                          'Negative_Review'              : 'str',
                          'Review_Total_Negative_Word_Counts' : 'int',
                          'Total_Number_of_Reviews'      : 'int',
                          'Positive_Review'              : 'str',
                          'Review_Total_Positive_Word_Counts' : 'int',
                          'Total_Number_of_Reviews_Reviewer_Has_Given' : 'int',
                          'Reviewer_Score'               : 'float',
                          'Tags'                         : 'str',
                          'days_since_review'            : 'str',
                          'lat'                          : 'float',
                          'lng'                          : 'float'})

@dataclass(frozen=True)
class model_conf:
    random_seed : int = 42