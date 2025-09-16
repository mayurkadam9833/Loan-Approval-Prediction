import pandas as pd
import streamlit as st 
from src.Loan_Approval_Prediction.pipeline.prediction_pipeline import PredictionPipeline

st.title("Loan Approval Prediction")
st.markdown("This project predicts whether a loan application will be approved or rejected based on applicant details")

no_of_dependents=st.sidebar.slider(label="No of dependents",min_value=0,max_value=6)
education=st.sidebar.selectbox(label="Education",options=[" Graduate"," Not Graduate"])
self_employed=st.sidebar.selectbox(label="self employed",options=[" No"," Yes"])
income_annum=st.sidebar.number_input(label="income annum")
loan_amount=st.sidebar.number_input(label="loan amount")
loan_term=st.sidebar.slider(label="loan_term",min_value=1,max_value=20)
cibil_score=st.sidebar.number_input(label="cibil_score")
residential_assets_value=st.sidebar.number_input(label="residential_assets_value")
commercial_assets_value=st.sidebar.number_input(label="commercial_assets_value")
luxury_assets_value=st.sidebar.number_input(label="luxury_assets_value")
bank_asset_value=st.sidebar.number_input(label="bank_asset_value")


if st.button("Loan Status"):
    input_data=pd.DataFrame({
        "no_of_dependents":[no_of_dependents],
        "education":[education],
        "self_employed":[self_employed],
        "income_annum":[income_annum],
        "loan_amount":[loan_amount],
        "loan_term":[loan_term],
        "cibil_score":[cibil_score],
        "residential_assets_value":[residential_assets_value],
        "commercial_assets_value":[commercial_assets_value],
        "luxury_assets_value":[luxury_assets_value],
        "bank_asset_value":[bank_asset_value]
    })

    pred=PredictionPipeline()
    p=pred.prediction(input_data)

    if p == 0:
        st.write("We’re sorry, but based on your details, your loan is not likely to be approved.")
    
    else:
        st.write("Congratulations! Based on your details, your loan is likely to be approved.")



