import pandas as pd
from sqlalchemy import create_engine

# Load cleaned dataset
df = pd.read_csv("data/cleaned_matches.csv")

# PostgreSQL connection
username = "postgres"
password = "ipl123"
host = "localhost"
port = "5432"
database = "ipl_analytics"

engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database}"
)

# Load dataframe into PostgreSQL
df.to_sql("matches", engine, if_exists="replace", index=False)

print("Data loaded successfully into PostgreSQL!")