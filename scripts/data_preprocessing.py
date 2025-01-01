import pandas as pd
import numpy as np

def load_data(file_path):
    """Load raw data from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean the dataset by handling missing values and outliers."""
    df = df.dropna()  # Drop rows with missing values
    df = df[(np.abs(df - df.mean()) <= (3 * df.std())).all(axis=1)]  # Remove outliers
    return df

def save_data(df, file_path):
    """Save the processed data."""
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    data = load_data("../data/raw_data.csv")
    cleaned_data = clean_data(data)
    save_data(cleaned_data, "../data/processed_data.csv")
