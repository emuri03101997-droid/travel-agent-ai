def check_climate(data):
    city = data["to_city"]

    # Fake weather data (simulation)
    weather_data = {
        "New York": {"temp": "18°C", "weather": "Rain"},
        "London": {"temp": "12°C", "weather": "Cloudy"},
        "Cleveland": {"temp": "10°C", "weather": "Snow"},
        "Paris": {"temp": "20°C", "weather": "Sunny"}
    }

    result = weather_data.get(city, {"temp": "22°C", "weather": "Clear"})

    temp = result["temp"]
    condition = result["weather"]

    suggestion = ""

    if condition.lower() == "rain":
        suggestion = "Carry an umbrella ☔"
    elif condition.lower() == "snow":
        suggestion = "Wear warm clothes 🧥"
    elif condition.lower() == "sunny":
        suggestion = "Use sunscreen 😎"
    else:
        suggestion = "Carry light clothing 👍"

    return f"""
Destination: {city}
Temperature: {temp}
Weather: {condition}
Suggestion: {suggestion}
"""