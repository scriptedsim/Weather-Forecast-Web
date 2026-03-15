import streamlit as st

st.title("Weather Forecast For The Next Days")

place = st.text_input(label="Place:")
days = st.slider(min_value=1, max_value=5, step=1, label="Forecast days:", help="Select the number of forecast days")
data = st.selectbox(label="Select data to view",options=("Temperature", "Sky"))

st.title(f"{data} for the next {days} days in {place}")