# import pandas as pd

# df=pd.read_csv("data/hacker_news.csv")
# # print(df.tail())

# titles=df["title"]
# print(titles)

import pandas as pd

# Read csv file
df = pd.read_csv("data/hacker_news.csv")

# Display first five rows
print("First 5 rows:")
print(df.head())

# Count rows and columns
rows, cols = df.shape
print("\nNumber of rows:", rows)
print("Number of columns:", cols)

# Get title column as pandas series
titles = df["title"]
print("\nTitle Series:")
print(titles)

# Filter titles containing Python
python_titles = df[
    df["title"].str.contains("Python", case=False, na=False)
]

print("\nTitles containing Python:")
print(python_titles["title"])

# Filter titles containing JavaScript
javascript_titles = df[
    df["title"].str.contains("JavaScript", case=False, na=False)
]

print("\nTitles containing JavaScript:")
print(javascript_titles["title"])

# Basic information about dataset
print("\nDataset Info:")
print(df.info())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Top posts by points
print("\nTop posts by points:")
print(df.sort_values(by="points", ascending=False))

# Average comments and points
print("\nAverage Comments:",
      df["num_comments"].mean())

print("Average Points:",
      df["points"].mean())