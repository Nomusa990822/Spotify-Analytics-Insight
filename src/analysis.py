import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load cleaned dataset.
    """
    try:
        df = pd.read_csv(file_path)
        print("✅ Cleaned data loaded")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        raise


def bpm_analysis(df: pd.DataFrame):
    """
    Analyze BPM vs average streams.
    """
    result = df.groupby("bpm_range")["streams"].mean()

    plt.figure()
    result.plot(kind="bar")
    plt.title("BPM Range vs Average Streams")
    plt.xlabel("BPM Range")
    plt.ylabel("Average Streams")
    plt.tight_layout()
    plt.savefig("visuals/bpm_vs_streams.png")
    plt.close()

    print("📊 BPM analysis complete")


def explicit_analysis(df: pd.DataFrame):
    """
    Compare explicit vs clean songs.
    """
    if "explicit" in df.columns:
        result = df.groupby("explicit")["streams"].mean()

        plt.figure()
        result.plot(kind="bar")
        plt.title("Explicit vs Clean Songs (Average Streams)")
        plt.xlabel("Explicit")
        plt.ylabel("Average Streams")
        plt.tight_layout()
        plt.savefig("visuals/explicit_vs_streams.png")
        plt.close()

        print("📊 Explicit analysis complete")


def genre_analysis(df: pd.DataFrame):
    """
    Analyze genre distribution.
    """
    if "primary_genre" in df.columns:
        result = df["primary_genre"].value_counts()

        plt.figure()
        result.plot(kind="bar")
        plt.title("Genre Distribution")
        plt.xlabel("Genre")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig("visuals/genre_distribution.png")
        plt.close()

        print("📊 Genre analysis complete")


def valence_analysis(df: pd.DataFrame):
    """
    Analyze valence vs streams relationship.
    """
    if "valence" in df.columns:
        plt.figure()
        plt.scatter(df["valence"], df["streams"])
        plt.title("Valence vs Streams")
        plt.xlabel("Valence")
        plt.ylabel("Streams")
        plt.tight_layout()
        plt.savefig("visuals/valence_vs_streams.png")
        plt.close()

        print("📊 Valence analysis complete")


def summary_statistics(df: pd.DataFrame):
    """
    Print summary statistics.
    """
    print("\n📊 Summary Statistics:")
    print(df.describe())


def main():
    file_path = "data/processed/cleaned_data.csv"

    df = load_data(file_path)

    summary_statistics(df)

    bpm_analysis(df)
    explicit_analysis(df)
    genre_analysis(df)
    valence_analysis(df)

    print("\n✅ All analyses completed. Visuals saved in /visuals folder.")


if __name__ == "__main__":
    main()
