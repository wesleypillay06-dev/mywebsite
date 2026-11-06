import streamlit as st

st.title("my first.website")


import streamlit as st
import pandas as pd

st.title("Retail Analytics Dashboard")

file = st.file_uploader("Upload CSV", type="csv")

if file is None: st.stop()

df = pd.read_csv(file)

st.subheader("Dataset")
st.dataframe(df)

st.subheader("First 5 Rows")
st.dataframe(df.head())

st.subheader("Statistics")
st.dataframe(df.describe())




st.subheader("Retail Dashboard")

st.metric("Total Revenue", df["Revenue_ZAR"].sum())

st.metric("Total Transactions", len(df))

st.metric("Items Sold", df["Quantity"].sum())

st.metric("Average Revenue", round(df["Revenue_ZAR"].mean(), 2))








st.subheader("Explore Your Data")

columns = st.multiselect("Select Columns", df.columns, default=df.columns)

category = st.selectbox("Select Category", df["Category"].unique())

filtered = df[df["Category"] == category]

st.dataframe(filtered[columns])







st.subheader("Retail Sales Charts")

# Bar chart - Revenue by Category
st.write("Revenue by Category")
sales = df.groupby("Category")["Revenue_ZAR"].sum()
st.bar_chart(sales)

# Line chart - Revenue by Date
st.write("Revenue Over Time")
sales = df.groupby("Date")["Revenue_ZAR"].sum()
st.line_chart(sales)

# Bar chart - Revenue by Store
st.write("Revenue by Store")
sales = df.groupby("Store")["Revenue_ZAR"].sum()
st.bar_chart(sales)

# Bar chart - Top 5 Products
st.write("Top 5 Products")
sales = df.groupby("Product")["Revenue_ZAR"].sum()
sales = sales.sort_values(ascending=False).head(5)
st.bar_chart(sales)

# Scatter chart - Quantity vs Revenue
st.write("Quantity vs Revenue")
st.scatter_chart(df, x="Quantity", y="Revenue_ZAR")

