from flask import Flask, request, render_template
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

        # Call orchestrator (this runs ALL agents)
        result = run_orchestrator(data)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
