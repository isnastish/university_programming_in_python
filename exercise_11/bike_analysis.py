import pandas as pd
import matplotlib.pyplot as plt


def analyze_bike_data() -> None:
    df = pd.read_csv("comptagevelo2010.csv")
    df = df.drop(df.columns[1], axis=1)
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
    df["Month"] = df["Date"].dt.month
    bike_paths = df.columns[1:-1]

    # 1. Total cyclists (all paths)
    print("Total cyclists (all paths):", int(df[bike_paths].sum().sum()))

    # 2. Total cyclists per path
    print("\nTotal cyclists per path:")
    for path, count in df[bike_paths].sum().sort_values(ascending=False).items():
        print("  " + path + ":", int(count))

    # 3. Most popular month (3 paths)
    print("\nMost popular month:")
    for path in ["Berri1", "Maisonneuve_1", "Maisonneuve_2"]:
        monthly = df.groupby("Month")[path].sum()
        print("  " + path + ": Month", monthly.idxmax())

    # 4. Plot: Berri1 by month
    monthly_berri = df.groupby("Month")["Berri1"].sum()
    plt.figure(figsize=(10, 6))
    plt.bar(monthly_berri.index, monthly_berri.values, color="steelblue")
    plt.xlabel("Month")
    plt.ylabel("Cyclists")
    plt.title("Berri1 - Monthly Traffic (2010)")
    plt.xticks(range(1, 13))
    plt.show()


if __name__ == "__main__":
    analyze_bike_data()
