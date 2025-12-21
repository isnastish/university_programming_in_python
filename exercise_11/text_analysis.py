import nltk
import matplotlib.pyplot as plt
from nltk.corpus import gutenberg, stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string


def find_most_common_words(
    n: int = 10,
) -> tuple[list[tuple[str, int]], list[tuple[str, int]]]:
    """Find the most common words in the text, both with and without stop words.

    Returns:
        A tuple of (top_n_with_punctuation, top_n_cleaned)
    """
    nltk.download("gutenberg", quiet=True)
    nltk.download("punkt", quiet=True)
    nltk.download("punkt_tab", quiet=True)
    nltk.download("stopwords", quiet=True)

    text = gutenberg.raw("chesterton-ball.txt")
    words = word_tokenize(text.lower())

    print("Total words:", len(words))

    # Top N most common words (with punctuation and stop words)
    word_counts = Counter(words)
    top_n = word_counts.most_common(n)
    print(f"\nTop {n} words (with punctuation):")
    for word, count in top_n:
        print("  " + word + ":", count)

    # Remove stop words and punctuation
    stop_words = set(stopwords.words("english"))
    clean_words = [
        w
        for w in words
        if w not in stop_words and w not in string.punctuation and w.isalpha()
    ]

    print("\nWords after cleaning:", len(clean_words))

    # Top N most common words (cleaned)
    clean_counts = Counter(clean_words)
    top_n_clean = clean_counts.most_common(n)
    print(f"\nTop {n} words (cleaned):")
    for word, count in top_n_clean:
        print("  " + word + ":", count)

    return top_n, top_n_clean


def display_word_frequency_graph(
    word_counts: list[tuple[str, int]], title: str, color: str = "steelblue"
) -> None:
    """Display a bar graph of word frequencies."""
    plt.figure(figsize=(10, 6))
    plt.bar([w[0] for w in word_counts], [w[1] for w in word_counts], color=color)
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    top_10, top_10_clean = find_most_common_words(10)

    display_word_frequency_graph(
        top_10, "Top 10 Most Common Words (with punctuation)", color="coral"
    )

    display_word_frequency_graph(
        top_10_clean, "Top 10 Most Common Words (without stop words)", color="green"
    )
