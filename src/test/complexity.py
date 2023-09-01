import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


class Complexity:
    """
    ### Description
    ---------------
    Class to compute complexity given a dataset of values and times.
    """
    def __init__(self, n_values: np.array, time_values: np.array) -> None:
        self.n_values = n_values
        self.time_values = time_values
        self.type_complexity = {
            "lineal": self.lineal_complexity,
            "quadratic": self.quadratic_complexity,
            "exponential": self.exponential_complexity,
            "logaritmic": self.logaritmic_complexity
        }
    
    def lineal_complexity(self, n_values, a, b):
        return a * n_values + b
    
    def quadratic_complexity(self, n_values, a, b):
        return a * np.power(n_values, 2) + b
    
    def exponential_complexity(self, n_values, a, b):
        return a * np.power(2, n_values) + b
    
    def logaritmic_complexity(self, n_values, a , b):
        return a * np.log(n_values) + b
    
    def compute(self, type: str):
        """
        """
        # Adjust the model to data.
        params, covariance = curve_fit(self.type_complexity[type], self.n_values, self.time_values)

        # Get adjusted values for `a` and `b`.
        a_fit, b_fit = params

        # Compute Coefficient of determination (R-squared).
        residuals = self.time_values - self.type_complexity[type](self.n_values, a_fit, b_fit)
        ss_res = np.sum(residuals ** 2)
        ss_tot = np.sum((self.time_values - np.mean(self.time_values)) ** 2)
        r_squared = 1 - (ss_res / ss_tot)

        # Plot results.
        plt.scatter(
            self.n_values, 
            self.time_values, 
            label="Data"
        )

        plt.plot(
            self.n_values, 
            self.type_complexity[type](self.n_values, a_fit, b_fit), 
            "r-", 
            label="Quadratic adjustment"
        )

        plt.xlabel("Size of the problem (n)")
        plt.ylabel("Running time (s)")
        plt.title(f"R-squared = {r_squared}")
        plt.legend()
        plt.show()

        # Print results.
        print(f"Adjusted model coefficients (a, b): {a_fit}, {b_fit}")
        print(f"Coefficient of determination (R-squared): {r_squared}")


df = pd.read_csv("result/complexity_10000_1000000_10000.csv")
complexity = Complexity(
    n_values=np.array(df["people"]),
    time_values=np.array(df["time"])
)
complexity.compute(type="quadratic")