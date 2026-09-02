import streamlit as st
import pickle
import pandas as pd

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗"
)

# -----------------------------
# Load trained model
# -----------------------------
model = pickle.load(open("Working_File.pkl", "rb"))

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("cars.xls")

# -----------------------------
# Clean data
# -----------------------------

# Remove rows where important columns are missing
df = df.dropna(subset=["company", "name", "fuel_type"])

# Remove numeric values from company column
df = df[
    ~df["company"].astype(str).str.strip().str.match(r"^\d+(\.\d+)?$")
]

# Remove numeric values from car name column
df = df[
    ~df["name"].astype(str).str.strip().str.match(r"^\d+(\.\d+)?$")
]

# -----------------------------
# Title
# -----------------------------
st.title("🚗 Car Price Prediction")
st.write("Enter the car details to predict its price.")

# -----------------------------
# Company / Brand
# -----------------------------
companies = sorted(
    df["company"].astype(str).str.strip().unique()
)

company = st.selectbox(
    "Select Company",
    companies
)

# -----------------------------
# Car Name based on Company
# -----------------------------
cars = sorted(
    df[df["company"].astype(str).str.strip() == company]["name"]
    .astype(str)
    .str.strip()
    .unique()
)

name = st.selectbox(
    "Select Car",
    cars
)

# -----------------------------
# Other inputs
# -----------------------------
year = st.number_input(
    "Year",
    min_value=1990,
    max_value=2026,
    value=2018,
    step=1
)

kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=30000,
    step=1000
)

# -----------------------------
# Fuel Type
# -----------------------------
fuel_types = sorted(
    df["fuel_type"].astype(str).str.strip().unique()
)

fuel_type = st.selectbox(
    "Fuel Type",
    fuel_types
)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "name": [name],
        "company": [company],
        "year": [year],
        "kms_driven": [kms_driven],
        "fuel_type": [fuel_type]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Estimated Car Price: ₹{prediction[0]:,.0f}"
    )