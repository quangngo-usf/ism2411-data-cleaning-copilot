## ism2411-data-cleaning-copilot

This project contains a small data-cleaning pipeline written in Python.  
It loads a messy CSV file of sales data, applies several cleaning steps, and exports a cleaned CSV.

## Project Structure
ism2411-data-cleaning-copilot/
├── data/
│ ├── raw/
│ │ └── sales_data_raw.csv
│ └── processed/
│ └── sales_data_clean.csv
├── src/
│ └── data_cleaning.py
├── README.md
└── reflection.md

## How to Run the Script

1. Install Python 3

Make sure Python 3 is installed on your system.

2. Install Dependencies

This project uses pandas:

pip install pandas

3. Run the Script
python src/data_cleaning.py

4. Output

After running, the cleaned CSV file will be saved in:

data/processed/sales_data_clean.csv