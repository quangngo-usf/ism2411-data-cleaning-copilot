import pandas as pd
from pathlib import Path


# Load CSV file
# Purpose: load a CSV file from a given path and return a pandas DataFrame

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
# Copilot suggested simple replace spaces with underscores
# I added .str.replace("-", "_") to handle dashes as well


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
    # Only drop columns that exist
    cols_to_check = [c for c in ["price", "quantity"] if c in df.columns]

    if cols_to_check:
        df = df.dropna(subset=cols_to_check)

    return df



# Save cleaned file

def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Cleaned file saved to: {output_path}")



# Main Script

if __name__ == "__main__":
    raw_path = r"C:\Users\nhatq\Downloads\Python for Business\ism2411-data-cleaning-copilot\data\raw\sales_data_raw.csv"
    cleaned_path = r"C:\Users\nhatq\Downloads\Python for Business\ism2411-data-cleaning-copilot\data\processed\sales_data_clean.csv"

    
    

    


    # Load raw
    df = load_data(raw_path)

    # Standardize names
    df = clean_column_names(df)

    # Rename into standard names
    df = rename_columns(df)

    # Clean values
    df = handle_missing_values(df)

    # Save output
    save_cleaned_data(df, cleaned_path)

    print("\nDONE! Your data is cleaned successfully.\n")
    print("Final columns:", df.columns.tolist())
