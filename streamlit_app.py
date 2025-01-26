import streamlit as st
from app.itinerary import generate_itinerary
from app.utils import validate_input
from app.settings import APP_NAME, DEBUG_MODE, DEFAULT_BUDGET, DEFAULT_DURATION

st.title(APP_NAME)

destination = st.text_input("Destination", placeholder="e.g., Paris, Tokyo")
duration = st.number_input("Trip Duration (days)", min_value=1, value=DEFAULT_DURATION, step=1)
budget = st.selectbox("Budget", ["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(DEFAULT_BUDGET))
preferences = st.text_area("Preferences", placeholder="e.g., Adventure, Food, History")

if st.button("Generate Itinerary"):
    is_valid, error_message = validate_input(destination, duration, budget, preferences)
    if not is_valid:
        st.error(error_message)
    else:
        st.write("Generating your itinerary...")

        itinerary = generate_itinerary(destination, duration, budget, preferences)

        st.subheader("Your Travel Itinerary")
        st.markdown(itinerary, unsafe_allow_html=True)  

        if DEBUG_MODE:
            st.write("Debugging information:")
            st.write(f"Destination: {destination}, Duration: {duration}, Budget: {budget}, Preferences: {preferences}")
