# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 18:24:58 2023

@author: anike
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('C:/F/Data science/ML Projets/2. Heart Disease Prediction/APP/heart_dis_trained_model.sav','rb'))


def heart(input_data):

     #change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

     #reshaping the numpy array as we are predicting for only one instance
    input_data_reshaped =  input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)

    print(prediction)
    
    #prints 0 so our model is predicting right
    if(prediction[0]==0):
       return 'This Person Does Not have Heart Disease'
    else:
       return 'This Person has Heart Disease'
       

def main():
     
    st.title('Heart_disease_prediction_webAPP')
    
    age= st.text_input('Age of the person: ')
    sex= st.text_input('Sex of the patient: ')
    cp= st.text_input(' Chest pain type experienced by the patient.: ')
    trestbps= st.text_input('Resting blood pressure (in mm Hg) of the patient.: ')
    chol= st.text_input('Serum cholesterol level: ')
    fbs= st.text_input(' Fasting blood sugar level : ')
    restecg= st.text_input('Resting electrocardiographic results of the patient.: ')
    thalach= st.text_input('Maximum heart rate achieved by the patient.: ')
    exang= st.text_input('Exercise-induced angina: ')
    oldpeak= st.text_input(' ST depression induced by exercise relative to rest.: ')
    slope= st.text_input('Slope of the peak exercise ST segment.: ')
    ca= st.text_input('Number of major vessels (0-3) colored by fluoroscopy.: ')
    thal= st.text_input('Thalassemia - a blood disorder : ')
    
    
    Diagnosis = ''
    
    if (st.button('Heart_Disease_Test_result')):
        Diagnosis = heart([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
    
        
    st.success(Diagnosis)





if __name__=='__main__':
    main()    
