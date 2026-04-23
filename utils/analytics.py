import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run_analytics(accounts, transactions):
    balances = np.array([acc["balance"] for acc in accounts])

    print("Total balance:", balances.sum())
    print("Average balance:", balances.mean())
    print("Max balance:", balances.max())
    print("Min balance:", balances.min())

    df = pd.DataFrame(accounts)
    print("\nAccount type grouping:")
    print(df.groupby("type")["balance"].sum())

    # charts
    plt.bar(df["name"], df["balance"])
    plt.title("Balance Chart")
    plt.show()

    df["type"].value_counts().plot.pie()
    plt.title("Account Types")
    plt.show()