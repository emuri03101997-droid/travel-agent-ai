from agents.requirement_checker import check_requirements
from agents.planning_agent import create_plan
from agents.flight_agent import search_flights
from agents.hotel_agent import search_hotels
from agents.climate_agent import check_climate


def run_orchestrator(data):

    # STEP 1: Check requirements
    check = check_requirements(data)

    if check != "All requirements satisfied":
        return check

    # STEP 2: Create plan
    plan = create_plan(data)

    # STEP 3: Get flights
    flights = search_flights(data)

    # STEP 4: Get hotels
    hotels = search_hotels(data)

    # STEP 5: Get climate info
    climate = check_climate(data)

    # STEP 6: Combine results into final output
    result = f"""
================ TRAVEL PLAN ================

🧭 PLAN:
{plan}

✈️ FLIGHTS:
Airline: {flights[0]['airline']}
Route: {flights[0]['route']}
Price: {flights[0]['price']}

🏨 HOTEL:
Hotel: {hotels[0]['hotel']}
Price: {hotels[0]['price']}
Rating: {hotels[0]['rating']}

🌦️ WEATHER:
{climate}

============================================
"""

    return result