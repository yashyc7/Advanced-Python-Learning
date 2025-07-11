from scipy import integrate
import numpy as np

# Define a function to integrate
def f(x):
    return x**x  # simple function: x²

# Integrate from x=0 to x=3
result, error = integrate.quad(f, 0, 3)

print("Area under curve =", result)
