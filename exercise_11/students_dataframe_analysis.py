import pandas as pd

students = {
    "Petrov": {
        "height": 185.5,
        "age": 17,
        "grade": 11,
        "avg_score": 10.5,
        "scholarship": 2500,
    },
    "Ivanov": {
        "height": 182.0,
        "age": 16,
        "grade": 10,
        "avg_score": 11.2,
        "scholarship": 3000,
    },
    "Sidorov": {
        "height": 180.0,
        "age": 17,
        "grade": 11,
        "avg_score": 9.8,
        "scholarship": 2000,
    },
    "Kozlov": {
        "height": 178.5,
        "age": 16,
        "grade": 10,
        "avg_score": 8.5,
        "scholarship": 1500,
    },
    "Volkov": {
        "height": 175.0,
        "age": 17,
        "grade": 11,
        "avg_score": 11.8,
        "scholarship": 3500,
    },
    "Sokolov": {
        "height": 173.5,
        "age": 16,
        "grade": 10,
        "avg_score": 7.2,
        "scholarship": 1000,
    },
    "Lebedev": {
        "height": 171.0,
        "age": 17,
        "grade": 11,
        "avg_score": 10.0,
        "scholarship": 2200,
    },
    "Orlov": {
        "height": 169.5,
        "age": 16,
        "grade": 10,
        "avg_score": 9.5,
        "scholarship": 1800,
    },
    "Volnov": {
        "height": 167.0,
        "age": 17,
        "grade": 11,
        "avg_score": 6.8,
        "scholarship": 800,
    },
    "Medvedev": {
        "height": 165.0,
        "age": 16,
        "grade": 10,
        "avg_score": 12.0,
        "scholarship": 4000,
    },
    "Kovalenko": {
        "height": 177.0,
        "age": 17,
        "grade": 11,
        "avg_score": 8.9,
        "scholarship": 1600,
    },
    "Shevchenko": {
        "height": 183.0,
        "age": 16,
        "grade": 10,
        "avg_score": 10.8,
        "scholarship": 2800,
    },
}


def analyze_students() -> None:
    # Convert to DataFrame
    df = pd.DataFrame.from_dict(students, orient="index").reset_index()
    df.columns = ["surname"] + list(df.columns[1:])

    # Add calculated columns
    df["annual_scholarship"] = df["scholarship"] * 12
    df["performance"] = df["avg_score"].apply(
        lambda x: "Excellent" if x >= 10.5 else ("Good" if x >= 8 else "Satisfactory")
    )

    # Basic analysis
    print("=== BASIC ANALYSIS ===")
    print(f"\nFirst 3 rows:\n{df.head(3)}")
    print(f"\nData types:\n{df.dtypes}")
    print(f"\nShape: {df.shape}")
    print(f"\nDescriptive statistics:\n{df.describe().round(2)}")

    # Filtering
    print("\n=== FILTERING ===")
    print(
        f"\nScholarship > 2000:\n{df[df['scholarship'] > 2000][['surname', 'scholarship']]}"
    )

    # Sorting
    print("\n=== SORTING ===")
    print(
        f"\nBy scholarship (desc):\n{df.sort_values('scholarship', ascending=False)[['surname', 'scholarship']]}"
    )

    # Grouping
    print("\n=== GROUPING ===")
    print(
        f"\nAverage by grade:\n{df.groupby('grade')[['avg_score', 'scholarship']].mean().round(2)}"
    )

    # Aggregation
    print("\n=== AGGREGATION ===")
    print(f"Max scholarship by grade:\n{df.groupby('grade')['scholarship'].max()}")
    print(f"\nUnique ages: {df['age'].nunique()}")
    print(f"Total scholarship fund: {df['scholarship'].sum()} UAH/month")


if __name__ == "__main__":
    analyze_students()
