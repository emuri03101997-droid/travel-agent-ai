from agents.climate_agent import check_climate
from agents.hotel_agent import search_hotels
from flask import Flask, request, render_template
from agents.requirement_checker import check_requirements
from agents.planning_agent import create_plan
from agents.flight_agent import search_flights
from orchestrator import run_orchestrator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        data = {
            "from_city": request.form.get("from_city"),
            "to_city": request.form.get("to_city"),
            "date": request.form.get("date"),
            "travelers": request.form.get("travelers"),
            "budget": request.form.get("budget")
        }

        check = check_requirements(data)

        if check != "All requirements satisfied":
            result = check
        else:
            result =run_orchestrator(data)
            flights = search_flights(data)
            hotels = search_hotels(data)
            climate = check_climate(data)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask is working!"

if __name__ == "__main__":
    app.run(debug=True)
