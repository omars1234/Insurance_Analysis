import streamlit as st
from predict_agecat import predict_agecat
from predict_area import predict_area
from predict_gender import predict_gender
from predict_numclaims import predict_numclaims
from predict_page import predict_frequency
from predict_veh_body import predict_Veh_Body
from predict_severity import predict_severity
from predict_veh_age import predict_vehicle_age
 

select_to_predict=st.sidebar.selectbox("Select Target Feature",["Severity","Frequency","Gender-Male or Female",
                                                                "Age Category","Area","Number Of Claims","Vehicle Body","Vehicle Age"])



if select_to_predict =="Severity" :
    predict_severity()

elif select_to_predict=="Frequency":
    predict_frequency()
    

elif select_to_predict=="Gender-Male or Female":
    predict_gender() 

elif select_to_predict=="Age Category":
    predict_agecat() 

elif select_to_predict=="Area":
    predict_area()

elif select_to_predict=="Number Of Claims":
    predict_numclaims()

elif select_to_predict=="Vehicle Body":
    predict_Veh_Body() 

elif select_to_predict=="Vehicle Age":
    predict_vehicle_age()                     

