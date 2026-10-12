
from app import app

app.config["TESTING"] = True

with app.test_client() as client:
    # Mark attendance for a test student
    marked = client.post(
        "/chat",
        json={
            "message": "Mark attendance for FinalTestStudent Present 2026-10-10"
        }
    )
    print("Mark attendance:", marked.get_json())

    # Check attendance percentage
    percentage = client.post(
        "/chat",
        json={
            "message": "What is the attendance percentage for FinalTestStudent?"
        }
    )
    print("Attendance percentage:", percentage.get_json())

    # View attendance records
    records = client.post(
        "/chat",
        json={
            "message": "Show attendance records for FinalTestStudent"
        }
    )
    print("Attendance records:", records.get_json())
