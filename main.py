
import numpy as np
from sklearn.linear_model import LinearRegression

def generate_data(a, noise, num_points):
    """
    Generates synthetic data based on y = ax + b with some noise.
    We'll fix b for simplicity for now.
    """
    b = 5 # Fixed intercept for now
    x = np.linspace(0, 10, num_points)
    noise_values = np.random.normal(0, noise, num_points)
    y = a * x + b + noise_values
    return x.reshape(-1, 1), y

def train_model(x, y):
    """
    Trains a simple linear regression model.
    """
    model = LinearRegression()
    model.fit(x, y)
    return model

if __name__ == '__main__':
    # Example usage
    a_param = 2.5
    noise_param = 1.5
    points_param = 50

    # Generate data
    x_data, y_data = generate_data(a_param, noise_param, points_param)

    # Train model
    lr_model = train_model(x_data, y_data)

    # Print results
    print(f"Original line: y = {a_param}x + 5")
    print(f"Regression line: y = {lr_model.coef_[0]:.2f}x + {lr_model.intercept_:.2f}")
