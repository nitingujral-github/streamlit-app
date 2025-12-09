# 1. Streamlit runs a lightweight web server and auto-updates UI when code changes.
# 2. You don’t need HTML/CSS/JS — just Python.
# 3. Each widget (like st.button) can trigger Python logic instantly.

# Steps to run
# 1. pip install streamlit
# 2. streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np

# Set page title and layout 
st.set_page_config(page_title="Streamlit Basics Demo1", layout="centered")

# Title and header
st.title("📊 Simple Streamlit UI Example")
st.header("Welcome to Streamlit Tutorial!")

# Display text and markdown
st.write("Streamlit makes it easy to build web apps using just Python.")
st.markdown("**Markdown** formatting works too! 💡")

# Take user input
name = st.text_input("Enter your first name:")

# Button to greet user
if st.button("Greet"):
    st.success(f"Hello, {name}! 👋 Welcome to Streamlit!")

# Add a slider widget
age = st.slider("Select your age:", 1, 100, 25)
st.write(f"Your age is: {age}")

# Add a select box
color = st.selectbox("Pick your favorite color:", ["Red", "Blue", "Green"])
st.info(f"You chose {color}. Nice choice!")

# Add a checkbox
if st.checkbox("Show a fun fact"):
    st.write("💡 Streamlit was launched in 2019 and is now used by millions!")

# --- Add Charts Section ---
st.subheader("📈 Let's explore some charts")

# Create random data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

# Line chart
st.line_chart(chart_data)

# Area chart
st.area_chart(chart_data)

# Bar chart
st.bar_chart(chart_data)

# Optionally, add data table
if st.checkbox("Show raw data"):
    st.dataframe(chart_data)
