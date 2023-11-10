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
    test_image_name = "test_image1.jpg"
    image_path = os.path.join("resources", test_image_name)
    files = {
        "file": (test_image_name, open(image_path, "rb"), "image/jpeg")
    }  # TODO: understand better

    # Send a POST request to the /upload endpoint
    response = client.post("/v1/detections", files=files)  # TODO: understand better

    output_file_path = os.path.join("test_outputs", test_image_name)
    with open(output_file_path, "wb") as f:
        f.write(response.content)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
