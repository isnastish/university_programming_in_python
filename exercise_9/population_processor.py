import csv
from typing import List, Dict, Union


def read_csv_file(filename: str) -> List[Dict[str, str]]:
    data = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
    except OSError as e:
        print(f"Error reading file {filename}: {e}")
        raise

    return data


def display_csv_content(data: List[Dict[str, str]]) -> None:
    if not data:
        print("No data to display.")
        return

    print("\n" + "=" * 80)
    print("CSV File Content:")
    print("=" * 80)

    headers = list(data[0].keys())
    print(" | ".join(headers))
    print("-" * 80)

    for row in data:
        values = [str(row.get(header, "")) for header in headers]
        print(" | ".join(values))

    print("=" * 80)


def find_ukraine_population_data(
    data: List[Dict[str, str]],
    indicator: str = "Population, total",
    country: str = "Ukraine",
    start_year: int = 1991,
    end_year: int = 2019,
) -> List[Dict[str, Union[str, float]]]:
    result: List[Dict[str, Union[str, float]]] = []

    for row in data:
        if (
            row.get("Country Name", "").strip() == country
            and row.get("Indicator Name", "").strip() == indicator
        ):
            for year in range(start_year, end_year + 1):
                value = row.get(str(year), "").strip()
                if value:
                    try:
                        population = float(value)
                        result.append(
                            {
                                "Year": str(year),
                                "Population": population,
                                "Country": country,
                                "Indicator": indicator,
                            }
                        )
                    except ValueError:
                        continue
            break

    return result


def find_min_max_values(
    data: List[Dict[str, Union[str, float]]],
) -> Dict[str, Dict[str, Union[str, float]]]:
    min_record = min(data, key=lambda x: x["Population"])
    max_record = max(data, key=lambda x: x["Population"])

    return {"min": min_record, "max": max_record}


def write_results_to_csv(
    results: Dict[str, Dict[str, Union[str, float]]], output_filename: str
) -> None:
    try:
        with open(output_filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["Type", "Year", "Population", "Country", "Indicator"]
            )
            writer.writeheader()

            min_row = results["min"].copy()
            min_row["Type"] = "Minimum"
            writer.writerow(min_row)

            max_row = results["max"].copy()
            max_row["Type"] = "Maximum"
            writer.writerow(max_row)

        print(f"\nResults written to {output_filename} successfully.")
    except OSError as e:
        print(f"Error writing to file {output_filename}: {e}")
        raise


def main():
    input_filename = "population_data.csv"
    output_filename = "ukraine_population_results.csv"

    try:
        csv_data = read_csv_file(input_filename)
        display_csv_content(csv_data)

        ukraine_data = find_ukraine_population_data(csv_data)
        print(f"\nFound {len(ukraine_data)} data points for Ukraine (1991-2019):")
        for record in ukraine_data:
            print(f"Year: {record['Year']}, Population: {record['Population']:,.0f}")

        min_max = find_min_max_values(ukraine_data)
        print("\n" + "=" * 60)
        print("RESULTS:")
        print("=" * 60)
        print(f"Minimum Population: {min_max['min']['Population']:,.0f} in {min_max['min']['Year']}")
        print(f"Maximum Population: {min_max['max']['Population']:,.0f} in {min_max['max']['Year']}")
        print("=" * 60)

        write_results_to_csv(min_max, output_filename)

    except OSError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
