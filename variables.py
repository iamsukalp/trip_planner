import json


with open("src/hobbies_and_interests.json", "r") as file:
    hobbies_and_interests = json.load(file)

with open("src/country_codes.json", "r") as json_file:
    country_codes = json.load(json_file)


default_message = """
🌍 Crew AI Travel Itinerary Tool 🧳

Overview:
The Crew AI Travel Itinerary Tool uses advanced language models to create personalized travel plans. It integrates weather forecasts and news updates to tailor itineraries based on your interests and preferences.

Key Features:
Personalized Itineraries: Input origin, destination, dates, and interests for customized plans.
Weather Integration: Real-time forecasts for activity suggestions and packing tips.
News Insights: Current events enhance cultural experiences and safety awareness.
Interactive Interface: Streamlit platform for user-friendly navigation.

How to Use:

Input Details: Enter origin, destination, dates, and interests.
Generate Itinerary: Click "Generate Itinerary" to start planning.
Review Suggestions: Explore activities, attractions, and dining options.
Customize: Adjust the itinerary to suit preferences.
Save and Share: Easily save or share the finalized itinerary.

Benefits:

Efficiency: AI-assisted planning saves time.
Personalization: Recommendations tailored to your preferences.
Real-time Updates: Stay informed with weather and news insights.
Plan your next adventure seamlessly with the Crew AI Travel Itinerary Tool! 🌟

"""
