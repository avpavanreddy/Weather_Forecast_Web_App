import streamlit as st

st.title("Weather Forecast For The Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the no of days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for next {days} days in {place}: ")

