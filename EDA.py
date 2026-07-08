import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset.csv")   # Replace with your actual file name

print(df.head())
print(df.info())
print(df.shape)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove the currency symbol and convert to f
# Remove any non-numeric characters except the decimal point
df["Price"] = df["Price"].str.replace(r"[^0-9.]", "", regex=True)
df["Price"] = df["Price"].astype(float)

print("\nUpdated Data Types:")
print(df.dtypes)
# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())
# Histogram (Price Distribution)
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], bins=10, kde=True)
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.savefig("price_histogram.png")
plt.show()
#BOX PLOT
plt.figure(figsize=(6,4))
sns.boxplot(x=df["Price"])
plt.title("Box Plot of Book Prices")
plt.savefig("price_boxplot.png")
plt.show()
#BAR CHART
plt.figure(figsize=(8,5))
sns.countplot(x="Rating", data=df, order=["One", "Two", "Three", "Four", "Five"])
plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.savefig("rating_distribution.png")
plt.show()