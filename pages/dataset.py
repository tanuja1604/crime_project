import streamlit as st
import pandas as pd

# Page Title
st.title("📂 Crime Dataset")

# Load Dataset
df = pd.read_csv("cleaned_crime_data1.csv")

# Display Shape
st.subheader("Dataset Shape")
st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])

# Display First 10 Rows
st.subheader("First 10 Records")
st.dataframe(df.head(10))

# Column Names
st.subheader("Column Names")
st.write(df.columns.tolist())

# Data Types
st.subheader("Data Types")
st.dataframe(df.dtypes)

# Missing Values
st.subheader("Missing Values")
st.dataframe(df.isnull().sum())

# Statistical Summary
st.subheader("Statistical Summary")
st.dataframe(df.describe())

# Show Full Dataset
if st.checkbox("Show Complete Dataset"):
    st.dataframe(df)