import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("T1.csv")
df['Date/Time'] = pd.to_datetime(df['Date/Time'], dayfirst=True)
print("Preview of the data:")
print(df.head())
print("\nSummary statistics:")
print(df.describe())
print("\nAvailable columns:")
print(df.columns)

plt.figure(figsize=(12, 5))
plt.plot(df['Date/Time'], df['LV ActivePower (kW)'], color='blue')
plt.title("Active Power Over Time")
plt.xlabel("Time")
plt.ylabel("Power (kW)")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
plt.hist(df['Wind Speed (m/s)'], bins=30, color='green')
plt.title("Distribution of Wind Speed")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()
