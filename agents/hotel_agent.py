def search_hotels(data):
    to_city = data["to_city"]

    hotels = [
        {
            "hotel": "Marriott",
            "price": "$150 per night",
            "rating": "4.5",
            "location": to_city
        },
        {
            "hotel": "Hilton",
            "price": "$130 per night",
            "rating": "4.3",
            "location": to_city
        },
        {
            "hotel": "Hyatt",
            "price": "$170 per night",
            "rating": "4.6",
            "location": to_city
        }
    ]

    return hotels