def validate_input(destination, duration, budget, preferences):
    """Validate user inputs."""
    if not destination or not preferences:
        return False, "Destination and preferences cannot be empty!"
    if duration <= 0:
        return False, "Duration must be at least 1 day!"
    if budget not in ["Low", "Medium", "High"]:
        return False, "Budget must be Low, Medium, or High!"
    return True, ""

def clean_response(response):
    """
    Clean and normalize the raw response from the model.
    """
    response = response.strip()
    response = response.replace("\n\n", "\n").replace("\n", " ")
    response = response.replace("  ", " ")  
    response = response.replace("*", "")  
    response = response.replace("###", "")  
    response = response.replace("U\nS\nD", "USD")  # Fix common currency artifact
    response = response.replace("\n", "")  # Flatten newlines further if needed
    return response
