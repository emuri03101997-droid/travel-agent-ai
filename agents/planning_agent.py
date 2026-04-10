def create_plan(data):
    plan = f"""
Travel Planning Steps:

1. Search flights from {data['from_city']} to {data['to_city']}
2. Book hotel for {data['travelers']} travelers
3. Check weather for {data['date']}
4. Suggest local activities in {data['to_city']}
5. Optimize trip within budget: {data['budget']}

Final Output:
- Flights planned
- Hotels planned
- Weather checked
- Activities suggested
"""
    return plan