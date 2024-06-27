# origin = input(
#     dedent(
#         """
#   From where will you be traveling from?
# """
#     )
# )
# cities = input(
#     dedent(
#         """
#   What are the cities options you are interested in visiting?
# """
#     )
# )
# date_range = input(
#     dedent(
#         """
#   What is the date range you are interested in traveling?
# """
#     )
# )
# interests = input(
#     dedent(
#         """
#   What are some of your high level interests and hobbies?
# """
#     )
# )

# trip_crew = TripCrew(origin, cities, date_range, interests)
# result = trip_crew.run()
# print("\n\n########################")
# print("## Here is you Trip Plan")
# print("########################\n")
# print(result)


import streamlit as st

# Define a sample dictionary
data = {
    "Option 1": ["Value A", "Value B", "Value C"],
    "Option 2": ["Value X", "Value Y", "Value Z"],
}


# Function to get values based on key selected
def get_values(key):
    return data[key]


# Streamlit app
def main():
    st.title("Dictionary Example")

    # Selectbox to choose key
    selected_key = st.selectbox("Select a key", list(data.keys()))

    # Multiselect to display values based on selected key
    selected_values = st.multiselect("Select values", get_values(selected_key))

    # Display selected key and values
    st.write("Selected Key:", selected_key)
    st.write("Selected Values:", selected_values)


if __name__ == "__main__":
    main()
