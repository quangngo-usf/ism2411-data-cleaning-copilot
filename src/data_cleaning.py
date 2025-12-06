import pandas as pd
from pathlib import Path


# Load CSV file
def load_data(file_path):
    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    return pd.read_csv(file)


# Clean column names
def clean_column_names(df):
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


# Rename known columns
def rename_columns(df):
    df = df.rename(columns={
        "qty": "quantity",
        "quantity_sold": "quantity",
        "price($)": "price",
        "unit_price": "price",
        "amount": "total_amount"
    })
    return df


# Handle missing values
def handle_missing_values(df):
    cols_to_check = [c for c in ["price", "quantity"] if c in df.columns]
    if cols_to_check:
        df = df.dropna(subset=cols_to_check)
    return df


# Convert price and quantity to numeric
def convert_to_numeric(df):
    for col in ["price", "quantity"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


# Remove invalid rows
def remove_invalid_rows(df):
    if "price" in df.columns:
        df = df[df["price"] >= 0]
    if "quantity" in df.columns:
        df = df[df["quantity"] >= 0]
    return df


# Save cleaned file
def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Cleaned file saved to: {output_path}")


# Main Script
if __name__ == "__main__":
    raw_path = r"C:\Users\nhatq\Downloads\Python for Business\ism2411-data-cleaning-copilot\data\raw\sales_data_raw.csv"
    cleaned_path = r"C:\Users\nhatq\Downloads\Python for Business\ism2411-data-cleaning-copilot\data\processed\sales_data_clean.csv"

    df = load_data(raw_path)
    df = clean_column_names(df)
    df = rename_columns(df)
    df = convert_to_numeric(df)
    df = handle_missing_values(df)
    df = remove_invalid_rows(df)

    save_cleaned_data(df, cleaned_path)

    print("Cleaning complete. First few rows:")
    print(df.head())
