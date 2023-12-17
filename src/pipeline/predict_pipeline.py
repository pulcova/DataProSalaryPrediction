import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self, features):
        try:
            model_path='artifacts\model.pkl'
            preprocessor_path='artifacts\preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e, sys)
    
class CustomData:
    def __init__(
        self,
        sex: str,
        designation: str,
        age: float,
        unit: str,
        ratings: float,
        past_experience: float       
    ):
        self.sex = sex
        self.designation = designation
        self.age = age
        self.unit = unit
        self.ratings = ratings
        self.past_experience = past_experience
        
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "SEX": [self.sex],
                "DESIGNATION": [self.designation],
                "AGE": [self.age],
                "UNIT": [self.unit],
                "RATINGS": [self.ratings],
                "PAST EXP": [self.past_experience]
            }
            
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)