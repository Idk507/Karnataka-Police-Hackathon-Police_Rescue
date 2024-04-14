import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

st.title("Future crime pattern prediction ")

# Load the trained ARIMA model
with open(r"C:\Users\hp\Desktop\project\model\arima\arima_model.pkl", 'rb') as f:
    model_fit = pickle.load(f)

# Define number of future periods for forecasting
future_steps = st.number_input("Enter number of months to forecast:", value=12, min_value=1, step=1)
#start_date_input = st.date_input("Enter start date for the forecast:", value=pd.Timestamp.today())

# Convert the user input date to a pandas Timestamp for compatibility
start_date = pd.to_datetime("2024-03-2")

# Forecast future crime patterns
future_forecast = model_fit.forecast(steps=future_steps)

# Get the dates for the forecasted period
future_dates = pd.date_range(start=start_date, periods=future_steps + 1, freq='ME')[1:]
# Plot forecasted values
plt.figure(figsize=(10, 6))
plt.plot(future_dates, future_forecast, label="Forecast")
#plt.fill_between(future_dates, conf_int[:, 0], conf_int[:, 1], color='gray', alpha=0.3, label='95% Confidence Interval')
plt.legend()
plt.title("Future Crime Forecast")
plt.xlabel("Date")
plt.ylabel("Predicted Crime Count")
st.pyplot(plt)

# Display forecasted values
st.write(f"Forecasted values for the next {future_steps} months:")
st.write(future_forecast)

