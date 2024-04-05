import numpy as np                    # np is an alias pointing to numpy
import matplotlib.pyplot as plt

def generate_AR3(phi, n):
    # Generate white noise
    epsilon = np.random.normal(size=n)
    
    # Initialize time series with zeros
    X = np.zeros(n)
    
    # Generate AR(3) process
    for t in range(3, n):
        X[t] = phi[0]*X[t-1] + phi[1]*X[t-2] + phi[2]*X[t-3] + epsilon[t]
    return X

# Generate random AR parameters
phi = np.random.uniform(-1, 1, size=3)

# Check stationarity
characteristic_poly = np.poly1d([1, -phi[0], -phi[1], -phi[2]])
roots = np.roots(characteristic_poly)

if np.all(np.abs(roots) > 1):
    print("AR(3) process is stationary.")
else:
    print("AR(3) process is not stationary. Please try again with different parameters.")

# Generate AR(3) process
n = 100
AR3_process = generate_AR3(phi, n)

# Plot the time series
plt.plot(AR3_process)
plt.title("AR(3) process")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()
