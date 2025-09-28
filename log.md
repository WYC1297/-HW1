# Log

## Step 1: Initial Python Script (Data and Model)

- **File Created:** `main.py`
- **Purpose:** To handle the core logic for data generation and the linear regression model.
- **Libraries Used:** `numpy`, `scikit-learn`.
- **Details:**
    - Implemented a `generate_data` function to create synthetic data points around a line `y = ax + b` with a specified amount of noise.
    - Implemented a `train_model` function that takes the generated data and fits a `LinearRegression` model.
    - Added a main execution block (`if __name__ == '__main__':`) to demonstrate the functionality by generating data, training the model, and printing the original and fitted line equations.

## Step 2: Streamlit Web Application

- **File Created:** `app.py`
- **Purpose:** To create an interactive web interface for the linear regression tool.
- **Libraries Used:** `streamlit`, `matplotlib`.
- **Details:**
    - Imported functions from `main.py`.
    - Used `st.title` and `st.header` to structure the app according to CRISP-DM steps.
    - Added `st.slider` widgets to allow users to control the parameters: slope `a`, noise, and number of points.
    - Called the `generate_data` and `train_model` functions to get the data and the model.
    - Used `matplotlib` to create a plot showing the generated data, the "true" line, and the fitted regression line.
    - Displayed the plot in the Streamlit app using `st.pyplot`.
    - Showed the original and fitted line equations as text.

## Step 3: Dependencies

- **File Created:** `requirements.txt`
- **Purpose:** To list the Python libraries required to run the application.
- **Libraries Listed:**
    - `streamlit`
    - `scikit-learn`
    - `numpy`
    - `matplotlib`
- **Details:** This file allows for easy installation of all necessary dependencies using the command `pip install -r requirements.txt`.