import numpy as np
import pickle
import streamlit as st

# Pickle is used to load the saved model , streamlit for deployment

# loading the saved model
loan_model =  pickle.load(open('D:/NEW PROJECT/loan_model.sav' ,'rb'))

#  Creating a function for prediction
def loan_prediction(input_data):

    input_data = (0, 0, 0, 1, 0, 2900, 0.0, 71.0, 360.0, 1.0, 0)

    # Changing the input data to numpy array
    np_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    np_array_reshaped = np_array.reshape(1, -1)

    prediction = loan_model.predict(np_array_reshaped)
    print(prediction)

    if (prediction[0] == 1):
        return 'Loan is approved'
    else:
        return 'Loan is rejected'

def main():

  # giving a title
  st.title('Loan Status Prediction')

  #   Getting the input data
  Gender=st.text_input('Gender')
  Married=st.text_input('Maritial status')
  Dependents=st.text_input('Dependents')
  Education=st.text_input('Education')
  Self_Employed=st.text_input('Self_Employed')
  ApplicantIncome=st.text_input('ApplicantIncome')
  CoapplicantIncome=st.text_input('CoapplicantIncome')
  LoanAmount =st.text_input('LoanAmount')
  Loan_Amount_Term=st.text_input('Loan_Amount_Term')
  Credit_History=st.text_input('Credit_History')
  Property_Area=st.text_input('Property_Area')

  # Code for prediction
  loan = ''

   # Creating a button for prediction

  if st.button('Loan Status Result'):
       loan = loan_prediction([Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount ,
                               Loan_Amount_Term, Credit_History, Property_Area,])

  st.success(loan)

if(__name__ == '__main__'):
    main()