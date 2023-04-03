import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast For The Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the no of days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for next {days} days in {place}: ")

if place:
    try:
        filtered_data = get_data(place, days, option)

        if option == 'Temperature':
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y= temperatures, labels={"x": "Date",
                                                              "y": "Temperature"})
            st.plotly_chart(figure)

        if option == 'Sky':
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png",
            }
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            images_path = [images[condition] for condition in sky_conditions]
            st.image(images_path, width=115)
    except KeyError:
        st.write(f"{place} does not exist")
