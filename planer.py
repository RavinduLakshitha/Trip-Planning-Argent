import os
from groq import Client as Groq
from config import GROQ_API_KEY

os.environ['GROQ_API_KEY'] = GROQ_API_KEY

client = Groq()

def generate_trip_plan(destination):
    """Generate a 7-day trip itinerary using Groq API."""
    prompt = f"""
    Plan a detailed 7-day itinerary for a trip to {destination}.
    Include morning, afternoon, and evening activities, local cuisine recommendations, and travel tips.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": "You are an expert travel planner."},
                  {"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    destination = input("Enter the trip destination: ")
    print("\nGenerating your 7-day trip plan...\n")
    
    trip_plan = generate_trip_plan(destination)
    
    print(trip_plan)