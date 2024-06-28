import streamlit as st  # type: ignore
from variables import country_codes, hobbies_and_interests, default_message
from datetime import datetime
from allcities import cities
from tripCrew import TripCrew


st.set_page_config(layout="wide", page_title="Trip Planner", page_icon="📅")
countries = list(country_codes)

today = datetime.now().date()

if "plan" not in st.session_state:
    st.session_state.plan = ""


def get_city_list(country):
    if not country:
        return []
    try:
        results = cities.filter(country_code=country_codes[country])
        city_list = [result.name for result in results]
        return city_list
    except Exception as e:
        return []


def app_ui():
    col1, col2 = st.columns([1, 1])

    with col2:
        st.title("Trip Planner Crew")
        st.write("-------------------------------")

        col211, col212 = st.columns([1, 1])
        with col211:
            o_country = st.selectbox(
                "Select Origin Country",
                countries,
                key="oCountry",
            )
        oCityList = get_city_list(o_country)
        with col212:
            origin = st.selectbox(
                "From where will you be traveling from?",
                oCityList,
                index=0,
                placeholder="Select Origin City",
                key="oCity",
            )

        col221, col222 = st.columns([1, 1])
        with col221:
            d_country = st.selectbox(
                "Select Destination Country",
                countries,
                key="dCountry",
            )
            dCityList = get_city_list(d_country)
        with col222:
            des_cities = st.multiselect(
                "What are the cities options you are interested in visiting?",
                dCityList,
                key="dCity",
            )
        date_range = st.date_input(
            "What is the date range you are interested in traveling?",
            min_value=today,
            value=[today, datetime(2023, 12, 31)],
            key="DateRange",
        )
        interests = st.multiselect(
            "What are some of your high-level interests and hobbies?",
            hobbies_and_interests,
            key="Interests",
        )
        col231, col232 = st.columns([0.82, 0.18])
        with col232:
            if st.button("Plan the trip", key="Submit"):
                trip_crew = TripCrew(origin, des_cities, date_range, interests)
                result = trip_crew.run()
                st.session_state.plan = result

    with col1:

        with st.container(height=550, border=True):
            if len(st.session_state.plan) > 1:
                st.write(st.session_state.plan)
            else:
                st.write(default_message)


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    app_ui()
