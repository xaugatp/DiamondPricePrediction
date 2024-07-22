import os 
import sys 
import pickle
import numpy as np 
import pandas as pd
from src.exception import CustomException 
from src.logger import logging
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    
    except Exception as e: 
        raise CustomException(e, sys)
    
    
def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for model_name, model in models.items():
            # Train model
            model.fit(X_train, y_train)
            
            # Predict Testing data
            y_test_pred = model.predict(X_test)
        
            # Get R2 scores for test data
            test_model_score = r2_score(y_test, y_test_pred)
        
            report[model_name] = test_model_score
    
        return report
    
    except Exception as e:
        logging.info("Exception occurred during model training")
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise CustomException(e,sys)