import streamlit as st 
import pandas as pd 
import joblib # type: ignore

# Load model (must include preprocessing if categorical data exists)
model = joblib.load("fraud_detection_model.pkl")

st.title("Fraud Detection Prediction App")

st.markdown("Please Enter the transaction details and use predict button")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", 'TRANSFER', 'CASH_OUT', 'DEPOSIT'])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,  
        "newbalanceDest": newbalanceDest
    }])

    # Predict
    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: {int(prediction)}")

    if prediction == 1:
        st.error("⚠️ This transaction might be fraudulent!")
    else:
        st.success("✅ This transaction looks legitimate.")
