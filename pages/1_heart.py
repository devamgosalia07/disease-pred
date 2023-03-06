import numpy as np
import pickle
import streamlit as st


# loading the saved model
model = pickle.load(open('heart_disease_model.sav', 'rb'))


# creating a function for Prediction

def heart_disease_model(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
         print('The Person does not have a Heart Disease')
    else:
         print('The Person has Heart Disease')
  
    
  
def main():
    
    
    # giving a title
    st.title('heart Disease Prediction Web App')
    
    
    # getting the input data from the user
    
    
    age = st.text_input('Age')
        

    sex = st.text_input('Sex')
        

    cp = st.text_input('Chest Pain types')
  
    trestbps = st.text_input('Resting Blood Pressure')
        

    chol = st.text_input('Serum Cholestoral in mg/dl')
        

    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        

    restecg = st.text_input('Resting Electrocardiographic results')

    thalach = st.text_input('Maximum Heart Rate achieved')
  
    exang = st.text_input('Exercise Induced Angina')

    oldpeak = st.text_input('ST depression induced by exercise')
   
   
    ca = st.text_input('Major vessels colored by flourosopy')
  
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    