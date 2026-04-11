from agents.flight_agent import search_flights
from agents.hotel_agent import search_hotels
from agents.climate_agent import check_climate

# Sample input data (this is your "keys")
data = {
    "from_city": "Cleveland",
    "to_city": "New York",
    "date": "2026-05-10",
    "travelers": "2",
    "budget": "1500"
}

print("=========== FLIGHT AGENT ===========")
flights = search_flights(data)
for f in flights:
    print(f)

print("\n=========== HOTEL AGENT ===========")
hotels = search_hotels(data)
for h in hotels:
    print(h)

print("\n=========== CLIMATE AGENT ===========")
climate = check_climate(data)
print(climate)