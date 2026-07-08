import pytest
import os
import sys

# Add src to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from scoring import calculate_ids

def test_calculate_ids_japan_mock():
    # Japan has high import concentration (e.g. middle east), high chokepoint exposure, moderate reserves
    japan_data = {
        "imports": [
            {"volume": 1200000, "source": "Saudi Arabia"},
            {"volume": 800000, "source": "UAE"},
            {"volume": 400000, "source": "Qatar"}
        ],
        "chokepoint_exposure": 0.85, # 85% through Hormuz/Malacca
        "reserve_days": 120 # Strategic reserves
    }
    score = calculate_ids(japan_data)
    # HHI = (12/24)^2 + (8/24)^2 + (4/24)^2 = 0.25 + 0.111 + 0.027 = 0.388 -> * 40 = 15.5
    # Chokepoint = 0.85 * 40 = 34
    # Reserve = (120/90) clamped to 1.0 -> 1.0 * 20 = 20
    # Total = 20 (base) + 15.5 + 34 - 20 = 49.5
    assert 40 < score < 60

def test_calculate_ids_usa_mock():
    # USA has high diversification (domestic + import), low chokepoint exposure, high reserves
    usa_data = {
        "imports": [
            {"volume": 3500000, "source": "Canada"},
            {"volume": 800000, "source": "Mexico"},
            {"volume": 400000, "source": "Saudi Arabia"}
        ],
        "chokepoint_exposure": 0.15,
        "reserve_days": 150
    }
    score = calculate_ids(usa_data)
    assert score < 40 # Should be lower risk than Japan

def test_empty_data():
    score = calculate_ids({})
    assert score == 0.0
