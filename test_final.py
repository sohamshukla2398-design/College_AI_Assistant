
from app import app

app.config["TESTING"] = True

with app.test_client() as client:
    # Test homepage
    home = client.get("/")
    print("Homepage:", home.status_code)

    # Test empty message handling
    empty = client.post("/chat", json={"message": ""})
    print("Empty message:", empty.status_code)
    print("Empty response:", empty.get_json())

    # Test calculator
    calc = client.post("/chat", json={"message": "25 * 16"})
    print("Calculator:", calc.status_code)
    print("Calculator response:", calc.get_json())

    # Test timetable
    timetable = client.post(
        "/chat",
        json={"message": "Show my timetable for Tuesday"}
    )
    print("Timetable:", timetable.status_code)
    print("Timetable response:", timetable.get_json())
