import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
import pytest 
from app.itinerary import generate_itinerary

def test_itinerary():
    destination = "India"
    duration = 2
    budget = "High"
    preferences = "Adventure, Food, History"
    
    result = generate_itinerary(destination, duration, budget, preferences)
    assert result is not None
    assert "India" in result['text']