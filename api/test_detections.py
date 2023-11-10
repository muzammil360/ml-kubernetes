import os

from fastapi.testclient import TestClient

from .server import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_post_detections():
    # send an image with multipart file upload
    image_path = os.path.join("resources", "test_image1.jpg")
    files = {
        "file": ("test_image1.jpg", open(image_path, "rb"), "image/jpeg")
    }  # TODO: understand better

    # Send a POST request to the /upload endpoint
    response = client.post("/v1/detections", files=files)  # TODO: understand better

    with open("received_image.jpg", "wb") as f:
        f.write(response.content)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
