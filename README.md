📊 Lagos Bread Price Data Analysis

This simple Python script uses pandas to analyze bread price entries for Lagos, Nigeria from a national food price dataset.

🔍 What It Does
	•	Loads and parses a CSV file containing food price data.
	•	Filters data to:
	•	Focus on Lagos State.
	•	Include only valid entries with bread prices.
	•	Adds a year column from the price_date field.
	•	Outputs:
	•	The number of bread price entries per year.
	•	The number of bread price entries recorded after 2021.

🧰 Requirements
	•	Python 3.7+
	•	pandas

Install dependencies:

pip install pandas

📂 Input

Make sure you have a CSV file named:

NGA_RTFP_mkt_2007_2025-06-16.csv

in the same directory as the script. The file should contain at least the following columns:
	•	adm1_name (State name)
	•	bread (Bread price)
	•	price_date (Date of record)

▶️ Usage

Run the script:

python script_name.py

Replace script_name.py with your actual filename.

📈 Sample Output

Bread entries per year:
2007     5
2008    10
...
2024    42
2025    17

Entries after 2021: 94


