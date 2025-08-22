from dataclasses import dataclass

@dataclass
class HotelReviews_Raw():
    Hotel_Address                             : str   # Address of hotel.
    Additional_Number_of_Scoring              : float # There are also some guests who just made a scoring on the service rather than a review. This number indicates how many valid scores without review in there.
    Review_Date                               : str   # Date when reviewer posted the corresponding review.
    Average_Score                             : float # Average Score of the hotel, calculated based on the latest comment in the last year.
    Hotel_Name                                : str   # Name of Hotel
    Reviewer_Nationality                      : str   # Nationality of Reviewer
    Negative_Review                           : str   # Negative Review the reviewer gave to the hotel. If the reviewer does not give the negative review, then it should be: 'No Negative'
    Review_Total_Negative_Word_Counts         : int   # Total number of words in the negative review.
    Total_Number_of_Reviews                   : int   # Total number of valid reviews the hotel has.
    Positive_Review                           : str   # Positive Review the reviewer gave to the hotel. If the reviewer does not give the negative review, then it should be: 'No Positive'
    Review_Total_Positive_Word_Counts         : int   # Total number of words in the positive review.
    Total_Number_of_Reviews_Reviewer_Has_Given: int   # Number of Reviews the reviewers has given in the past.
    Reviewer_Score                            : float # Score the reviewer has given to the hotel, based on his/her experience
    Tags                                      : str   # Tags reviewer gave the hotel.
    days_since_review                         : str   # Duration between the review date and scrape date.
    lat                                       : float # Latitude of the hotel
    lng                                       : float # longtitude of the hotel
