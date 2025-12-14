import csv
import matplotlib.pyplot as plt


def load_data_from_csv(filepath: str = "countries_data.csv"):
    data: dict[str, dict[int, int]] = {}
    years: list[int] = []

    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        countries = [col for col in fieldnames if col != "Year"]

        for country in countries:
            data[country] = {}

        for row in reader:
            year = int(row["Year"])
            years.append(year)
            for country in countries:
                data[country][year] = int(row[country])

    return years, data


years, data = load_data_from_csv()
ukraine_data = list(data["Ukraine"].values())
usa_data = list(data["USA"].values())


def plot_line_graphs():
    plt.figure(figsize=(12, 6))
    plt.plot(
        years,
        ukraine_data,
        linewidth=2.5,
        color="blue",
        marker="o",
        markersize=4,
        label="Ukraine",
        linestyle="-",
    )
    plt.plot(
        years,
        usa_data,
        linewidth=2.5,
        color="red",
        marker="s",
        markersize=4,
        label="USA",
        linestyle="-",
    )

    plt.xlabel("Year", fontsize=12, fontweight="bold")
    plt.ylabel("Children out of school, primary", fontsize=12, fontweight="bold")
    plt.title(
        "Children out of school, primary - Dynamics (2004-2023)",
        fontsize=14,
        fontweight="bold",
    )
    plt.grid(True, alpha=0.3, linestyle="--")
    plt.legend(loc="best", fontsize=11)
    plt.xticks(years[::2], rotation=45)
    plt.tight_layout()
    plt.show()


def plot_bar_chart(country_name: str) -> None:
    if country_name not in data:
        print(f"Error: Data for '{country_name}' not found.")
        print(f"Available countries: {', '.join(data.keys())}")
        return

    country_values = list(data[country_name].values())
    country_years = list(data[country_name].keys())

    bar_color = "green" if country_name.lower() == "usa" else "red"

    plt.figure(figsize=(12, 6))
    plt.bar(
        country_years,
        country_values,
        width=0.6,
        color=bar_color,
        edgecolor="black",
        linewidth=1.2,
    )

    plt.xlabel("Year", fontsize=12, fontweight="bold")
    plt.ylabel("Children out of school, primary", fontsize=12, fontweight="bold")
    plt.title(
        f"Children out of school, primary - {country_name} (2004-2023)",
        fontsize=14,
        fontweight="bold",
    )
    plt.grid(True, alpha=0.3, axis="y", linestyle="--")
    plt.xticks(country_years[::2], rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    print("=" * 60)
    print("World Bank Data Visualizer")
    print("Indicator: Children out of school, primary")
    print("=" * 60)

    print("\n1. Line graphs (Ukraine vs USA)")
    print("2. Bar chart (select country)")
    print("3. Exit")

    while True:
        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            plot_line_graphs()

        elif choice == "2":
            country = input("Enter country name (Ukraine/USA): ").strip()
            plot_bar_chart(country)

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
