import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
username = "postgres"
password = "ipl123"
host = "localhost"
port = "5432"
database = "ipl_analytics"

engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database}"
)

# Load data
query = "SELECT * FROM matches"
df = pd.read_sql(query, engine)

# Title
st.title("🏏 IPL Analytics Dashboard")

# Total matches
st.subheader("Total Matches")
st.write(df.shape[0])

# Top winning teams
st.subheader("Top Winning Teams")
top_teams = df['winner'].value_counts().head()
st.bar_chart(top_teams)