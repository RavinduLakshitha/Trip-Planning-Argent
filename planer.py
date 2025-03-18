import os
from groq import Client as Groq
from config import GROQ_API_KEY

os.environ['GROQ_API_KEY'] = GROQ_API_KEY

client = Groq()

def generate_trip_plan(destination, budget, transportation, accommodation):
    """Generate a 7-day trip plan based on budget, transportation, and accommodation using Groq API."""
    prompt = f"""
    Plan a detailed 7-day itinerary for a trip to {destination} within a {budget} budget.
    
    - Include morning, afternoon, and evening activities.
    - Suggest local cuisine recommendations.
    - Provide local transportation details based on the preference: {transportation}.
    - Suggest accommodation options based on the preference: {accommodation}.
    
    **Budget Guidelines:**
    - 'low': Budget-friendly places, street food, public transport, and hostels.
    - 'medium': A mix of affordable and premium options.
    - 'high': Luxury hotels, fine dining, and private transport.
    
    **Local Transportation Options:**
    - 'public': Suggest buses, metro, trains, and shared taxis.
    - 'private': Recommend rental cars, taxis, or personal drivers.
    - 'mixed': A combination of public and private transport.

    **Accommodation Options:**
    - 'hostel': Affordable dorm-style stays for budget travelers.
    - 'hotel': Comfortable mid-range hotels.
    - 'luxury': 5-star hotels and premium resorts.
    - 'Airbnb': Home rentals for a personalized experience.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": "You are an expert travel planner."},
                  {"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    destination = input("Enter the trip destination: ")
    budget = input("Enter your budget (low, medium, high): ")
    transportation = input("Enter your transportation preference (public, private, mixed): ")
    accommodation = input("Enter your accommodation preference (hostel, hotel, luxury, Airbnb): ")
    print("\nGenerating your 7-day trip plan...\n")
    
    trip_plan = generate_trip_plan(destination, budget, transportation, accommodation)
    
    print(trip_plan)