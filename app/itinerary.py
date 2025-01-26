from app.llama_api import parse_with_llm

def generate_itinerary(destination, duration, budget, preferences):
    try:
        
        response = parse_with_llm(destination, duration, budget, preferences)
        return response

    except Exception as e:
        return f"Error occurred in itinerary generation: {str(e)}"
