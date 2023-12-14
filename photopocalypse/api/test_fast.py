import pytest
from fastapi.testclient import TestClient
from photopocalypse.api.fast import app
import zipfile
from io import BytesIO
from fastapi import FastAPI, UploadFile, File


client = TestClient(app)

@pytest.fixture
def image_cache():
    return {
        "image1.jpg": b"image1_data",
        "image2.jpg": b"image2_data",
        "image3.jpg": b"image3_data",
    }

def test_upscale_images(image_cache):
    response = client.post("/upscale-images/", json=image_cache)
    assert response.status_code == 200

    # Check if the zip file is returned
    assert response.headers["Content-Type"] == "application/zip"

    # Check if the zip file contains the expected number of images
    with zipfile.ZipFile(BytesIO(response.content), "r") as zip_file:
        assert len(zip_file.namelist()) == len(image_cache)

    # Check if the images in the zip file are correct
    with zipfile.ZipFile(BytesIO(response.content), "r") as zip_file:
        for index, (filename, contents) in enumerate(image_cache.items()):
            image_data = zip_file.read(f"image_{index}.jpg")
            assert image_data == contents
