# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 12:37:44 2023

@author: NIKHIL
"""

import streamlit as st
import pickle
import sklearn



pickle_in = open('C:/Users/NIKHIL/OneDrive/Desktop/streamlit/classifier.pkl','rb')
classifier=pickle.load(pickle_in)


def predict_customer_RetentionPotential(OnlineCommunication, AutomaticRefill,
DoorstepDelivery, welcome_email_opened, no_of_customized_email,
no_of_customized_email_opened, no_of_customized_email_clicked,
TotalOrderQuantity, OrderFrequency, Average_Ordergap,
no_of_DayswithBusiness, no_of_MakingBusinessDays, City_CITY2,
City_CITY3, City_CITY4, PreferredDeliveryDay_Monday,
PreferredDeliveryDay_Saturday, PreferredDeliveryDay_Sunday,
PreferredDeliveryDay_Thursday, PreferredDeliveryDay_Tuesday,
PreferredDeliveryDay_Wednesday):
    
    prediction=classifier.predict([[OnlineCommunication, AutomaticRefill,
   DoorstepDelivery, welcome_email_opened, no_of_customized_email,
   no_of_customized_email_opened, no_of_customized_email_clicked,
   TotalOrderQuantity, OrderFrequency, Average_Ordergap,
   no_of_DayswithBusiness, no_of_MakingBusinessDays, City_CITY2,
   City_CITY3, City_CITY4, PreferredDeliveryDay_Monday,
   PreferredDeliveryDay_Saturday, PreferredDeliveryDay_Sunday,
   PreferredDeliveryDay_Thursday, PreferredDeliveryDay_Tuesday,
   PreferredDeliveryDay_Wednesday]])
    print(prediction)
    return prediction
    
    
    
def main():
    st.title("Customer_RetentionPotential_Prediction")
    html_temp = """
    <div style = "background-color:tomato;padding:10px">
    <h2 style = "color:white;text-align:center;">customer_RetentionPotential </h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    OnlineCommunication=st.text_input("OnlineCommunication","Type Here")
    AutomaticRefill=st.text_input("AutomaticRefill","Type Here")
    DoorstepDelivery=st.text_input("DoorstepDelivery","Type Here")
    welcome_email_opened=st.text_input("welcome_email_opened","Type Here")
    no_of_customized_email=st.text_input("no_of_customized_email","Type Here")
    no_of_customized_email_opened=st.text_input("no_of_customized_email_opened","Type Here")
    no_of_customized_email_clicked=st.text_input("no_of_customized_email_clicked","Type Here")
    TotalOrderQuantity=st.text_input("TotalOrderQuantity","Type Here")
    OrderFrequency=st.text_input("OrderFrequency","Type Here")
    Average_Ordergap=st.text_input("Average_Ordergap","Type Here")
    no_of_DayswithBusiness=st.text_input("no_of_DayswithBusiness","Type Here")
    no_of_MakingBusinessDays=st.text_input("no_of_MakingBusinessDays","Type Here")
    City_CITY2=st.text_input("City_CITY2","Type Here")
    City_CITY3=st.text_input("City_CITY3","Type Here")
    City_CITY4=st.text_input("City_CITY4","Type Here")
    PreferredDeliveryDay_Monday=st.text_input("PreferredDeliveryDay_Monday","Type Here")
    PreferredDeliveryDay_Saturday=st.text_input("PreferredDeliveryDay_Saturday","Type Here")
    PreferredDeliveryDay_Sunday=st.text_input("PreferredDeliveryDay_Sunday","Type Here")
    PreferredDeliveryDay_Thursday=st.text_input("PreferredDeliveryDay_Thursday","Type Here")
    PreferredDeliveryDay_Tuesday=st.text_input("PreferredDeliveryDay_Tuesday","Type Here")
    PreferredDeliveryDay_Wednesday=st.text_input("PreferredDeliveryDay_Wednesday","Type Here")
    
    result = ""
    if st.button("Predict"):
        result=predict_customer_RetentionPotential( OnlineCommunication, AutomaticRefill,
       DoorstepDelivery, welcome_email_opened, no_of_customized_email,
       no_of_customized_email_opened, no_of_customized_email_clicked,
       TotalOrderQuantity, OrderFrequency, Average_Ordergap,
       no_of_DayswithBusiness, no_of_MakingBusinessDays, City_CITY2,
       City_CITY3, City_CITY4, PreferredDeliveryDay_Monday,
       PreferredDeliveryDay_Saturday, PreferredDeliveryDay_Sunday,
       PreferredDeliveryDay_Thursday, PreferredDeliveryDay_Tuesday,
       PreferredDeliveryDay_Wednesday)
        
        
    #st.success('The Customer RetentionPotential level is {}'.format(result))
    st.success(f'The Customer RetentionPotential level is {"Low" if result == 0 else "High" if result == 1 else "Medium" if result == 2 else "Unknown"}')


    
    
    
    

if __name__=='__main__':
    main()



