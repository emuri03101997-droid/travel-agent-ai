def check_requirements(data):
    missing_fields = []

    if not data.get("from_city"):
        missing_fields.append("From City")

    if not data.get("to_city"):
        missing_fields.append("To City")

    if not data.get("date"):
        missing_fields.append("Date")

    if not data.get("travelers"):
        missing_fields.append("Travelers")

    if not data.get("budget"):
        missing_fields.append("Budget")

    if missing_fields:
        return f"Missing fields: {', '.join(missing_fields)}"

    return "All requirements satisfied"