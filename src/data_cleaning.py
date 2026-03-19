import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load dataset from CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        raise


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names (lowercase, underscores).
    """
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
    )
    return df


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename columns to consistent names for analysis.
    """
    column_mapping = {
        "total_streams_billions": "streams",
        "song_title": "track_name"
    }

    for old_col, new_col in column_mapping.items():
        if old_col in df.columns:
            df.rename(columns={old_col: new_col}, inplace=True)

    return df


def convert_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert relevant columns to numeric.
    """
    numeric_cols = [
        "streams",
        "bpm",
        "danceability",
        "energy",
        "valence",
        "acousticness"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def clean_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values.
    """
    before = df.shape[0]
    df = df.dropna()
    after = df.shape[0]

    print(f"🧹 Removed {before - after} rows with missing values")
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows.
    """
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]

    print(f"🧹 Removed {before - after} duplicate rows")
    return df


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create additional features for analysis.
    """
    if "bpm" in df.columns:
        df["bpm_range"] = pd.cut(
            df["bpm"],
            bins=[0, 80, 100, 120, 140, 200],
            labels=["Very Slow", "Slow", "Medium", "Fast", "Very Fast"]
        )

    return df


def save_data(df: pd.DataFrame, output_path: str):
    """
    Save cleaned dataset.
    """
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to {output_path}")


def main():
    input_path = "data/raw/spotify_alltime_top100_songs.csv"
    output_path = "data/processed/cleaned_data.csv"

    df = load_data(input_path)
    df = standardize_columns(df)
    df = rename_columns(df)
    df = convert_numeric(df)
    df = clean_missing_values(df)
    df = remove_duplicates(df)
    df = feature_engineering(df)

    save_data(df, output_path)


if __name__ == "__main__":
    main()
