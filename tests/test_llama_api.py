import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

import pytest
from app.llama_api import parse_with_llm

def test_parse_with_llm():
    destination = "India"
    duration = 2
    budget = "High"
    preferences = "Food, history"
    
    response = parse_with_llm(destination, duration, budget, preferences)
    assert response is not None
    assert "Itinerary" in response