import json
import matplotlib.pyplot as plt


def load_population_from_json(filepath: str = "population_data.json"):
    with open(filepath, "r") as f:
        return json.load(f)


def plot_population_pie_chart() -> None:
    data = load_population_from_json()

    for country, info in data["countries"].items():
        years = list(info["data"].keys())[::5]  # Every 5 years
        populations = [info["data"][y] for y in years]

        plt.figure(figsize=(10, 8))
        plt.pie(populations, labels=years, autopct="%1.1f%%", startangle=90)
        plt.title(f"Population Distribution - {country}")
        plt.show()


if __name__ == "__main__":
    plot_population_pie_chart()
