import pandas as pd

# Load the dataset
file_path = 'test.csv'
data = pd.read_csv(file_path)

# Convert columns to appropriate data types
data['Breakout (30Days)'] = pd.to_numeric(data['Breakout (30Days)'], errors='coerce')
data['LTP'] = pd.to_numeric(data['LTP'], errors='coerce')
data['RSI'] = pd.to_numeric(data['RSI'], errors='coerce')
data['Volume'] = data['Volume'].str.replace('x', '').astype(float)

# Filter 1: Conditions for upward trend
upward_trend = data[
    (data['MA-Signal'].str.startswith('Bull')) &                   # MA-Signal starts with "Bull"
    (data['RSI'] > 60) &                                           # RSI greater than 60
    (data['Volume'] > 1.0) &                                       # Volume greater than 1.x
    (data['Trend (30Days)'].isin(['Strong Up', 'Weak Up']))        # Trend (30Days) is "Strong Up" or "Weak Up"
].copy()
upward_trend.loc[:, 'LTP > Breakout'] = upward_trend['LTP'] > upward_trend['Breakout (30Days)']

# Filter 2: Conditions for downward trend
downward_trend = data[
    (data['MA-Signal'].str.startswith('Bear')) &                   # MA-Signal starts with "Bull"
    (data['RSI'] < 30) &                                           # RSI less than 30
    (data['Volume'] > 1.0) &                                       # Volume greater than 1.x
    (data['Trend (30Days)'].isin(['Strong Down', 'Weak Down']))    # Trend (30Days) is "Strong Down" or "Weak Down"
].copy()
downward_trend.loc[:, 'LTP < Breakout'] = downward_trend['LTP'] < downward_trend['Breakout (30Days)']

# Combine both filtered data
consolidated_data = pd.concat([upward_trend, downward_trend], ignore_index=True)

# Save the consolidated data to a CSV file
output_path = 'result.csv'
consolidated_data.to_csv(output_path, index=False)

print(f"Consolidated data saved to: {output_path}")
