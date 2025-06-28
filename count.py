import pandas as pd

# Load the dataset
df = pd.read_csv("NGA_RTFP_mkt_2007_2025-06-16.csv")

# Convert price_date to datetime
df['price_date'] = pd.to_datetime(df['price_date'], errors='coerce')

# Filter for Lagos and valid bread data
lagos = df[(df['adm1_name'] == 'Lagos') & df['bread'].notna()]

# Add year column
lagos['year'] = lagos['price_date'].dt.year

# Count bread entries per year
counts = lagos['year'].value_counts().sort_index()
print("Bread entries per year:\n", counts)

# Check how many entries exist after 2021
after_2021 = lagos[lagos['year'] > 2021]
print("\nEntries after 2021:", after_2021.shape[0])
