
import streamlit as st
import matplotlib.pyplot as plt
from main import generate_data, train_model

st.title('Simple Linear Regression with CRISP-DM')

st.header('1. Business Understanding')
st.write("The goal of this application is to provide an interactive tool to understand simple linear regression. Users can adjust parameters to see how they affect the model's fit.")

st.header('2. Data Understanding & 3. Data Preparation')
st.write("We generate synthetic data based on the equation `y = ax + b + noise`.")

# User Inputs
a_param = st.slider('Select the slope (a)', 0.0, 10.0, 2.5)
noise_param = st.slider('Select the noise level', 0.0, 5.0, 1.5)
points_param = st.slider('Select the number of data points', 10, 100, 50)

# Generate Data
x_data, y_data = generate_data(a_param, noise_param, points_param)

st.header('4. Modeling')
st.write("We use scikit-learn's LinearRegression model to fit a line to the data.")

# Train Model
lr_model = train_model(x_data, y_data)

st.header('5. Evaluation')
st.write("The plot below shows the original data, the true line, and the fitted regression line.")

# Plotting
fig, ax = plt.subplots()
ax.scatter(x_data, y_data, label='Generated Data')
ax.plot(x_data, a_param * x_data + 5, color='green', linestyle='--', label='True Line')
ax.plot(x_data, lr_model.predict(x_data), color='red', label='Regression Line')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
st.pyplot(fig)

st.write(f"**Original line equation:** `y = {a_param}x + 5`")
st.write(f"**Fitted regression line equation:** `y = {lr_model.coef_[0]:.2f}x + {lr_model.intercept_:.2f}`")

st.header('6. Deployment')
st.write("This application is deployed as a Streamlit web app.")

