import pickle
import streamlit as st
import pickle
import numpy as np
import pandas as pd
from xgboost import XGBRFRegressor,XGBClassifier
from sklearn.ensemble import (AdaBoostRegressor,BaggingClassifier,RandomForestClassifier)




agecat_model=pickle.load(open("C:/Users/Omar/Desktop/Note_Books/final_models/agecat_prediction_model.pkl","rb"))
area_model=pickle.load(open("C:/Users/Omar/Desktop/Note_Books/final_models/area_prediction_model.pkl","rb"))
gender_model=pickle.load(open("C:/Users/Omar/Desktop/Note_Books/final_models/gender_prediction_model.pkl","rb"))
numclaims_model=pickle.load(open("C:/Users/Omar/Desktop/Note_Books/final_models/numclaims_prediction_model.pkl","rb"))
veh_body_model=pickle.load(open("C:/Users/Omar/Desktop/Note_Books/final_models/veh_body_prediction_model.pkl","rb"))
vehage_model=pickle.load(open("C:/Users/Omar/Desktop/Note_Books/final_models/vehage_prediction_model.pkl","rb"))
severity_model=pickle.load(open("C:/Users/Omar/Desktop/Note_Books/final_models/Severity_final_model.pkl","rb"))
Frequency_model=pickle.load(open("C:/Users/Omar/Desktop/Note_Books/final_models/Frequency_final_model.pkl","rb"))
    
