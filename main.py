import streamlit as st
import plotly.express as px

st.title("Weather Forecast For The Next Days")

place = st.text_input(label="Place:")
days = st.slider(min_value=1, max_value=5, step=1, label="Forecast days:", help="Select the number of forecast days")
data = st.selectbox(label="Select data to view",options=("Temperature", "Sky"))

st.subheader(f"{data} for the next {days} days in {place}")

def get_data(days):
    dates = ["2025-03-15", "2025-03-16", "2025-03-17"]
    temperatures = [10, 11, 20]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t= get_data(days)


figure = px.line(x=d, y=t, labels={"x":"Dates", "y":"Temperatures"})
st.plotly_chart(figure)