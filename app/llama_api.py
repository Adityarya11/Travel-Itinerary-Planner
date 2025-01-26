from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from .utils import clean_response


template = """
You are an AI travel planner. Your job is to create highly personalized travel itineraries based on user preferences. 
Here are the instructions you should follow:
- You must generate a detailed day-by-day itinerary based on the user's inputs (destination, trip duration, budget, and preferences).
- Make sure to include attractions, activities, and food recommendations tailored to the user's preferences.
- If the user provides vague or unclear information, ask for clarification or make the best possible assumptions.

User's preferences: {user_prompt}
Task description: {task_description}
"""

model = OllamaLLM(model="llama3.1")

def format_response(response):
    """
    Structure the response into clear, readable sections.
    """
    
    response = clean_response(response)

    sections = response.split("Day ")
    formatted_response = ["### Day-by-Day Itinerary"]

    for section in sections:
        if section.strip():
            if "Budget Breakdown" in section:
                formatted_response.append("### Budget Breakdown")
                formatted_response.append(section.strip())
            else:
                formatted_response.append(f"Day {section.strip()}")

    return "\n\n".join(formatted_response)


def parse_with_llm(destination, duration, budget, preferences, task_description="Create a detailed day-by-day itinerary."):
    try:
        
        user_msg = f"I want to plan a {duration}-day trip to {destination}. My budget is {budget}, and I prefer {preferences}."

        if not preferences or preferences.lower() in ["no", "none"]:
            user_msg += "Please suggest activities that most travelers enjoy."
        
        chat_prompt = ChatPromptTemplate.from_template(template).format(
            user_prompt=user_msg,
            task_description=task_description,
        )

        
        response = model.invoke(chat_prompt)

        
        if not response:
            raise ValueError("Model failed to generate a response.")

        return format_response(response)

    except Exception as e:
        return f"Error occurred: {str(e)}"
