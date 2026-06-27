import streamlit as st
import joblib

# Load models
svm_model = joblib.load("models/linear_svm.pkl")
tfidf = joblib.load("models/tfidf.pkl")

# Title
st.title("📩 SMS / Email Spam Classifier")

st.write(
    "Enter a message and click Predict."
)

# Input box
user_text = st.text_area(
    "Enter your message"
)

# Predict button
if st.button("Predict"):

    vector = tfidf.transform([user_text])

    prediction = svm_model.predict(vector)[0]

    if prediction == 1:
        st.error("🚨 Spam Message")
    else:
        st.success("✅ Ham Message")