import pandas as pd

# Load dataset
matches = pd.read_csv("data/matches.csv")

print("Before Cleaning:")
print(matches.isnull().sum())

# Fill missing city values
matches['city'] = matches['city'].fillna("Unknown")

# Fill missing player_of_match
matches['player_of_match'] = matches['player_of_match'].fillna("Not Awarded")

# Fill missing winner
matches['winner'] = matches['winner'].fillna("No Result")

# Drop method column (too many nulls)
matches = matches.drop(columns=['method'])

print("\nAfter Cleaning:")
print(matches.isnull().sum())

# Save cleaned dataset
matches.to_csv("data/cleaned_matches.csv", index=False)

print("\nCleaned dataset saved successfully!")