import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast For The Next Days")

place = st.text_input(label="Place:")
forecast_days = st.slider(min_value=1, max_value=5, step=1, label="Forecast days:", help="Select the number of forecast days")
kind = st.selectbox(label="Select data to view",options=("Temperature", "Sky"))

st.subheader(f"{kind} for the next {forecast_days} days in {place}")

if place:
    filtered_data = get_data(place, forecast_days)

    if kind == "Temperature":
        temperature = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperature, labels={"x":"Dates", "y":"Temperatures"})
        st.plotly_chart(figure)

    if kind == "Sky":
        images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png", "Rain":"images/rain.png", "Snow":"images/snow.png"}
        sky = [dict["weather"][0]["main"] for dict in filtered_data]
        image_url = [images[condition] for condition in sky]
        st.image(image_url, width=115)


    
    