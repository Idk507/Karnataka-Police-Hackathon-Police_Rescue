import streamlit as st
import pickle
import pandas as pd

st.title("BEHAIVER PREDICTION")
 
 # Load the trained model
with open(r'C:\Users\hp\Desktop\project\model\accused behaiver\logistic_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create input fields
age = st.number_input("Enter age:", min_value=0)
sex = st.radio("Select sex:", ("FEMALE", "MALE"))
present_city = st.radio("Select present city:", ("Bengaluru City", "Other"))
present_state = st.radio("Select present state:", ("Karnataka", "Other"))

# Convert inputs to model format
sex_female = 1 if sex == 'FEMALE' else 0
sex_male = 1 if sex == 'MALE' else 0
city_bengaluru = 1 if present_city == 'Bengaluru City' else 0
state_karnataka = 1 if present_state == 'Karnataka' else 0

# Create a data frame for the input data
input_data = pd.DataFrame({
    'age': [age],
    'Sex_FEMALE': [sex_female],
    'Sex_MALE': [sex_male],
    'PresentCity_Bengaluru City': [city_bengaluru],
    'PresentState_Karnataka': [state_karnataka]
})

# Make a prediction
if st.button("Predict Behavioral Status"):
    prediction = model.predict(input_data)
    st.write(f"The predicted Behavioral Status is: {prediction[0]}")

