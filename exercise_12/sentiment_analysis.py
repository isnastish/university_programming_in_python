import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def download_nltk_resources() -> bool:
    """Downloads required NLTK resources."""
    try:
        nltk.download("vader_lexicon", quiet=True)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def get_sample_messages() -> list[str]:
    """Returns sample messages for demonstration."""
    return [
        "I love this product! It's absolutely amazing!",
        "This is the worst experience ever. Terrible service.",
        "The weather today is okay, nothing special.",
        "Just finished a great book. Highly recommend!",
        "I'm so frustrated with this software. It keeps crashing!",
        "Had lunch at the new restaurant. Food was decent.",
        "Congratulations on your promotion! You deserve it!",
        "The movie was boring and too long. Waste of time.",
        "Meeting scheduled for tomorrow at 3 PM.",
        "Thank you so much for your help! You're the best!",
        "I hate waiting in long lines. So annoying.",
        "The presentation went well. Good feedback.",
        "Feeling sad today. Nothing seems to go right.",
        "What a beautiful sunset! Nature is amazing.",
        "The pizza was cold and delivery took forever.",
    ]


def analyze_sentiment(message: str, analyzer: SentimentIntensityAnalyzer) -> dict:
    """Analyzes sentiment of a single message."""
    scores = analyzer.polarity_scores(message)
    compound = scores["compound"]

    if compound >= 0.05:
        classification = "Positive"
    elif compound <= -0.05:
        classification = "Negative"
    else:
        classification = "Neutral"

    return {
        "message": message,
        "positive": scores["pos"],
        "negative": scores["neg"],
        "neutral": scores["neu"],
        "compound": compound,
        "classification": classification,
    }


def analyze_all_messages(messages: list[str]) -> list[dict]:
    """Analyzes sentiment for all messages."""
    analyzer = SentimentIntensityAnalyzer()
    return [analyze_sentiment(msg, analyzer) for msg in messages]


def calculate_statistics(results: list[dict]) -> dict:
    """Calculates summary statistics from results."""
    total = len(results)
    positive = sum(1 for r in results if r["classification"] == "Positive")
    negative = sum(1 for r in results if r["classification"] == "Negative")
    neutral = sum(1 for r in results if r["classification"] == "Neutral")
    avg_compound = sum(r["compound"] for r in results) / total if total > 0 else 0

    return {
        "total": total,
        "positive": positive,
        "negative": negative,
        "neutral": neutral,
        "positive_pct": (positive / total * 100) if total > 0 else 0,
        "negative_pct": (negative / total * 100) if total > 0 else 0,
        "neutral_pct": (neutral / total * 100) if total > 0 else 0,
        "avg_compound": avg_compound,
    }


def display_results(results: list[dict], stats: dict) -> None:
    """Displays results in a formatted table."""
    print("\n" + "=" * 80)
    print(f"{'#':<4} {'Classification':<12} {'Compound':<10} {'Message':<50}")
    print("-" * 80)

    for i, r in enumerate(results, 1):
        msg = r["message"][:47] + "..." if len(r["message"]) > 50 else r["message"]
        print(f"{i:<4} {r['classification']:<12} {r['compound']:>8.3f}   {msg}")

    print("-" * 80)
    print(
        f"Total: {stats['total']} | "
        f"Positive: {stats['positive']} ({stats['positive_pct']:.1f}%) | "
        f"Negative: {stats['negative']} ({stats['negative_pct']:.1f}%) | "
        f"Neutral: {stats['neutral']} ({stats['neutral_pct']:.1f}%)"
    )


def create_visualization(stats: dict, output_path: str = "sentiment_chart.png") -> None:
    """Creates and saves visualization charts."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    labels = ["Positive", "Negative", "Neutral"]
    sizes = [stats["positive"], stats["negative"], stats["neutral"]]
    colors = ["#4CAF50", "#F44336", "#9E9E9E"]

    ax1.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
    ax1.set_title("Sentiment Distribution")

    bars = ax2.bar(labels, sizes, color=colors)
    ax2.set_ylabel("Count")
    ax2.set_title("Sentiment Count")

    for bar, value in zip(bars, sizes):
        ax2.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.1,
            str(value),
            ha="center",
            fontweight="bold",
        )

    plt.tight_layout()

    try:
        plt.savefig(output_path, dpi=150)
        print(f"\nChart saved to '{output_path}'")
    except IOError as e:
        print(f"Error saving chart: {e}")

    plt.show()


def get_user_choice(prompt: str, valid: list[str]) -> str:
    """Gets validated user input."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid:
            return choice
        print("Invalid choice.")


def get_messages_from_user() -> list[str]:
    """Gets messages from user input."""
    print("\nEnter messages (empty line to finish):")
    messages: list[str] = []
    while True:
        msg = input(f"{len(messages) + 1}: ").strip()
        if not msg:
            break
        messages.append(msg)
    return messages


def main() -> None:
    """Main program loop."""
    if not download_nltk_resources():
        return

    while True:
        print("\n[1] Sample messages  [2] Enter manually  [3] Exit")
        choice = get_user_choice("Choice: ", ["1", "2", "3"])

        if choice == "1":
            messages = get_sample_messages()
        elif choice == "2":
            messages = get_messages_from_user()
            if not messages:
                continue
        else:
            break

        try:
            results = analyze_all_messages(messages)
            stats = calculate_statistics(results)
        except Exception as e:
            print(f"Error: {e}")
            continue

        display_results(results, stats)

        if get_user_choice("\nShow and save chart? (y/n): ", ["y", "n"]) == "y":
            create_visualization(stats)


if __name__ == "__main__":
    main()
