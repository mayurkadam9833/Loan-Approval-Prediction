import pandas as pd
import streamlit as st 
from src.Loan_Approval_Prediction.pipeline.prediction_pipeline import PredictionPipeline

st.title("Loan Approval Prediction")
st.markdown("This project predicts whether a loan application will be approved or rejected based on applicant details")

Age=st.sidebar.number_input(label="Age",min_value=1,max_value=70)
Gender=st.sidebar.selectbox(label="Gender",options=["Male","Female"])
MaritalStatus=st.sidebar.selectbox(label="Marital Status",options=["Non-Married","Married"])
EducationLevel=st.sidebar.selectbox(label="Education Level",options=["High School","Bachelor","Master","PhD","Other"])
EmploymentStatus=st.sidebar.selectbox(label="Employment Status",options=["Unemployed","Employed","Self-employed","Retired","Student"])
AnnualIncome=st.sidebar.number_input(label="Annual Income")
LoanAmountRequested=st.sidebar.number_input(label="LoanAmount Requested")
PurposeOfLoan=st.sidebar.selectbox(label="Purpose Of Loan",options=["Personal","Home","Education","Car","Business"])
CreditScore=st.sidebar.number_input(label="Credit Score")
ExistingLoansCount=st.sidebar.number_input(label="Existing Loans Count")
LatePaymentsLastYear=st.sidebar.number_input(label="Late Payments LastYear")

if st.button("Loan Status"):
    input_data=pd.DataFrame(
        {
            "Age":[Age],
            "Gender":[Gender],
            "MaritalStatus":[MaritalStatus],
            "EducationLevel":[EducationLevel],
            "EmploymentStatus":[EmploymentStatus],
            "AnnualIncome":[AnnualIncome],
            "LoanAmountRequested":[LoanAmountRequested],
            "PurposeOfLoan":[PurposeOfLoan],
            "CreditScore":[CreditScore],
            "ExistingLoansCount":[ExistingLoansCount],
            "LatePaymentsLastYear":[LatePaymentsLastYear]
        }
    )

    pred=PredictionPipeline()
    p=pred.prediction(input_data)

    if p == 0:
        st.write("We’re sorry, but based on your details, your loan is not likely to be approved.")
    
    else:
        st.write("Congratulations! Based on your details, your loan is likely to be approved.")



