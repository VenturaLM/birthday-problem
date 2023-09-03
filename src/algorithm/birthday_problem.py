import os

import numpy as np
import pandas as pd
import plotly.express as px

class BirthdayProblem:
    """
    ### Description
    ---------------
    Class to represent the [birthday problem](https://en.wikipedia.org/wiki/Birthday_problem). The
    original problem is presented with the following values: `people=100` and `birthdays=365`, 
    having a probability of `p=0.5072` when 23 people are in the scenario.

    ### Parameters
    --------------
    - `people`: number of participants in the scenario.
    - `birthdays`: the range of possible unique birthdays (usually from 1 to 365).
    """
    def __init__(self, people: int, birthdays: int) -> None:
        # CHECKS
        # ------
        if not isinstance(people, int):
            raise TypeError(f"Argument 'people' must be of type 'int' (Current {type(people)}).")
        if people < 0:
            raise ValueError(f"Argument 'people' must be greater than 0 (Current {people}).")

        if not isinstance(birthdays, int):
            raise TypeError(f"Argument 'birthdays' must be of type 'int' (Current {type(birthdays)}).")
        if birthdays < 0:
            raise ValueError(f"Argument 'birthdays' must be greater than 0 (Current {birthdays}).")
        
        # CLASS ATTRIBUTES
        # ----------------
        self.people = people
        self.birthdays = birthdays
    
    def __repr__(self) -> str:
        return f"BirthdayProblem(people={self.people}, birthdays={self.birthdays})"

    def plot_solution(self, df) -> None:
        """
        ### Description
        ---------------
        Plots the birthday problem solution.

        ### Parameters
        --------------
        - `df`: Pandas DataFrame with data. It comes indexed as follows:

        |   | probability |   people  |
        |---| ----------- | --------- | 
        | 0 |    0.000000 |     1     |
        | 1 |    0.002740 |     2     |
        | 2 |    0.008204 |     3     |
        | 3 |    0.016356 |     4     |
        | 4 |    0.027136 |     5     |
        | ..|    ...      |     ...   |
        | 22|    0.507297 |     23    |
        | ..|    ...      |     ...   |
        | 99|    1.000000 |     100   |
        
        """
        # Create figure.
        fig = px.line(
            df,
            x="people",
            y="probability",
            template="plotly_dark",
        )
        
        # Updates some figure's parameters.
        fig.update_layout(
            title_text="Birthday problem",
            font=dict(family="LaTeX")
        )

        # Add an horizontal shape at p=0.5.
        fig.add_shape(
            type="line",
            x0=0,
            y0=0.5,
            x1=len(df),
            y1=0.5,
            line=dict(color="orange", width=2)
        )

        # Add a text annotation of p=0.5.
        fig.add_annotation(
            x=0, 
            y=0.5,
            text=f"Prob.: 0.5",
            showarrow=False,
            yshift=10
        )

        # Save image as '.svg' file.
        result_dir = "result"
        result_path = os.path.join(result_dir, "plot.svg")

        try:
            os.mkdir(result_dir)
            message = f"Success: '{result_dir}' created."
        except FileExistsError:
            message = f"'FileExistsError': '{result_dir}' already exists."
        # print(message)

        fig.write_image(result_path, format="svg")
        
        # Plot.
        fig.show()
        
    def solve(self) -> pd.DataFrame:
        """
        ### Description
        ---------------
        Method to solve the birthday problem given the initialization parameters. The total
        computational complexity of this code may be:

        `O(self.people) + O(self.people) + O(1) + O(self.people^2)` 
        
        thus,

        `2 * O(self.people) + O(1) + O(self.people^2)`
        """
        # Probability.
        p = float(1)

        # List saving the amount of participants.
        people_array = np.array(list(range(1, self.people + 1)))

        # List saving the probabilities.
        p_array = np.array(list())

        # Compute probability for each birthday.
        for i in range(1, self.people + 1):
            p = p * (self.birthdays + 1 - i) / self.birthdays

            p_array = np.append(p_array, float(1) - p)

        # Save data within Pandas DataFrame.
        data = {"probability": p_array, "people": people_array}
        df = pd.DataFrame(data)

        return df