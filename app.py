import streamlit as st
import numpy as np
import pickle

# Load trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Page title
st.set_page_config(page_title="Placement Predictor", layout="centered")
st.title("🎓 Student Placement Prediction App")

st.write("This app predicts whether a student is likely to be placed based on CGPA and IQ.")

# Input sliders
cgpa = st.slider("Select your CGPA", 0.0, 10.0, step=0.1)
iq = st.slider("Select your IQ", 70, 150, step=1)

if st.button("Predict Placement"):
    input_data = np.array([[cgpa, iq]])

    # Manual rule-based condition
    if iq > 100 and cgpa > 6:
        st.success("✅ You are likely to be placed! (Rule-Based)")
    else:
        # Use ML model if rule not satisfied
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.success("✅ You are likely to be placed!")
        else:
            st.warning("❌ You might not be placed. Keep learning!")


st.markdown("---")

