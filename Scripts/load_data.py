import pandas as pd
# Load dataset
matches = pd.read_csv("data/matches.csv")
# Basic info
print("Shape of dataset:")
print(matches.shape)
print("\nColumns:")
print(matches.columns)
# Missing values
print("\nMissing Values:")
print(matches.isnull().sum())
# Top 5 winners
print("\nTop 5 Teams with Most Wins:")
print(matches['winner'].value_counts().head())

# Seasons available
print("\nSeasons:")
print(matches['season'].unique())