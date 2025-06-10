import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect("../db/lesson.db")

query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

# Load data into DataFrame
df = pd.read_sql_query(query, conn)

# Add cumulative column
df['cumulative'] = df['total_price'].cumsum()

# Display DataFrame (optional — просто чтобы посмотреть)
print(df)

# Plot cumulative revenue vs. order_id
df.plot(x='order_id', y='cumulative', kind='line', title='Cumulative Revenue Over Orders')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue ($)')
plt.grid(True)
plt.show()

conn.close()
