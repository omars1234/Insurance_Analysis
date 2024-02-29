
import pickle
import streamlit as st
import numpy as np
import pandas as pd
from xgboost import XGBRFRegressor,XGBClassifier
from sklearn.ensemble import (AdaBoostRegressor,BaggingClassifier,RandomForestClassifier)
from sklearn.tree import DecisionTreeRegressor
from utilis import (gender_string_to_number,area_string_to_number,agecat_string_to_number,veh_age_string_to_number,
                    veh_body_string_to_number,numclaims_string_to_number)

veh_body_model=pickle.load(open("C:/Users/Omar/Desktop/Omar_Files/Python_Analysis/Auto_Insurance/final_models/veh_body_prediction_model.pkl","rb")) 

def predict_Veh_Body():
    st.title("Motor Insurance Prediction")
    st.subheader("Target Feature To Predict : Vehicle Body")

    veh_value=st.number_input("veh_values",0.0,34.560000)

    exposure=st.number_input("exposure",0.0,0.9999)

    numclaims=st.selectbox("select number of claims",["0","1","2","3"])

    claimcst0=st.number_input("claims_cost",0.0,55922.129883)
    
    veh_age=st.selectbox("select veh_age",["1","2","3","4"])

    area=st.selectbox("select area",['C', 'B', 'F', 'A', 'D', 'E'])

    agecat=st.selectbox("select age_category",["1","2","3","4","5","6"]) 

    gender=st.selectbox("select gender",["M","F"]) 

    severity=st.number_input("severity",0.0,55922.0) 

    frequincy=st.number_input("frequincy",0.0,1.0)

    #veh_value	exposure numclaims	claimcst0	veh_body	veh_age	gender	area	agecat	severity	frequincy


    columns=['veh_value','exposure','numclaims','claimcst0','veh_age','gender','area','agecat','severity','frequincy']

    ok=st.button("Predict")
    if ok:
         row=np.array([veh_value,exposure,numclaims,claimcst0,veh_age,gender,area,agecat,severity,frequincy])
         x=pd.DataFrame([row],columns=columns)
         st.dataframe(x)

         make_prediction=veh_body_model.predict([[
            veh_value,
            exposure,
            numclaims_string_to_number(numclaims),
            claimcst0,
            veh_age_string_to_number(veh_age),
            gender_string_to_number(gender),
            area_string_to_number(area),
            agecat_string_to_number(agecat),
            severity,
            frequincy]])[0]  

         st.write(f"The Expected Vehicle Body is {make_prediction}")



if __name__=="__main__" :
    predict_Veh_Body()
   
    


