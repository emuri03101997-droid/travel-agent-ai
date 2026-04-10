def search_flights(data):
    from_city = data["from_city"]
    to_city = data["to_city"]

    flights = [
        {"route": f"{from_city} → {to_city}", "price": "$220", "airline": "Delta"},
        {"route": f"{from_city} → {to_city}", "price": "$180", "airline": "United Airlines"},
        {"route": f"{from_city} → {to_city}", "price": "$250", "airline": "American Airlines"}
    ]

    return flights