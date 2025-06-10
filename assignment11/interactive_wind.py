# interactive_wind.py

import pandas as pd
import plotly.express as px
import plotly.data as pldata

# Load the built-in wind dataset from Plotly
df = pldata.wind(return_type='pandas')

# Display the first and last 10 rows of the dataset
print("FIRST 10 ROWS:\n", df.head(10))
print("\nLAST 10 ROWS:\n", df.tail(10))

# Clean the 'strength' column
# Convert strength categories like '0-1', '1-2', '6+' to numeric values
# We'll map ranges to their approximate midpoints and '6+' to 6.5

def convert_strength(val):
    if val == '6+':
        return 6.5
    elif '-' in val:
        start, end = val.split('-')
        return (float(start) + float(end)) / 2
    else:
        return float(val)  # fallback (not really used in this dataset)

df['strength'] = df['strength'].map(convert_strength)

# Create interactive scatter plot
fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs Frequency by Direction',
    hover_data=['direction', 'strength', 'frequency']
)

# Save as HTML and open in browser
fig.write_html("wind.html", auto_open=True)
