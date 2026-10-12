
from app import app

with app.test_client() as client:
    with open("documents/test.txt", "rb") as file:
        response = client.post(
            "/upload",
            data={"file": (file, "test.txt")},
            content_type="multipart/form-data"
        )

    print("Status Code:", response.status_code)
    print("Response:", response.get_json())
