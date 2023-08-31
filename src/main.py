import argparse

from core.birthday_problem import BirthdayProblem


def main():
    """
    ### Usage
    ---------
    >>> python3 src/main.py -p 100 -b 365
    """
    # Command line argument parser.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", 
        "--people", 
        type=int, 
        help="Number of participants in the scenario.",
        default=100
    )
    parser.add_argument(
        "-b", 
        "--birthdays", 
        type=int, 
        help="The range of possible unique birthdays (usually from 1 to 365).",
        default=365
    )

    args = parser.parse_args()

    # NOTE: Be cautious when increasing the parameter size: execution times can become lengthy, and 
    # furthermore, you might run out of memory.
    bp = BirthdayProblem(
        people=args.people,   # 1_000_000_000
        birthdays=args.birthdays   # (2 ** 256) - 1
    )

    # Run solve method.
    data = bp.solve()
    print(data)

    # Plot data.
    bp.plot_solution(df=data)

if __name__ == "__main__":
    main()