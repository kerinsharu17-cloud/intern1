import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("quotes_data.csv")

print("First 5 rows:")
print(data.head())

print("\nDataset Info:")
data.info()

print("\nSummary Statistics:")
print(data.describe(include="all"))

author_count = data['Author'].value_counts().head(10)

author_count.plot(kind='bar')
plt.title("Top Authors by Number of Quotes")
plt.xlabel("Author")
plt.ylabel("Count")

plt.show()
