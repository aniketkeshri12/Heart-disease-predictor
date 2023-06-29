# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 18:19:36 2023

@author: anike
"""

import numpy as np
import pickle

#loading the saved model
loaded_model = pickle.load(open('C:/F/Data science/ML Projets/2. Heart Disease Prediction/APP/heart_dis_trained_model.sav','rb'))

input_data = (50,0,1,120,244,0,1,162,0,1.1,2,0,2)
 #53,1,0,140,203,1,0,155,1,3.1,0,0,3 these are all features taken from dataset and its ouptup should be 0: No disease , lets see what our model predicts

 #change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

 #reshaping the numpy array as we are predicting for only one instance
input_data_reshaped =  input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)

print(prediction)
#prints 0 so our model is predicting right
if(prediction[0]==0):
   print('This Person Does Not have Heart Disease')
else:
   print('This Person has Heart Disease')




#can also check for the below Data of another Patient it will give Heart Disease
# 50,0,1,120,244,0,1,162,0,1.1,2,0,2 = > 1 : With heart Disease