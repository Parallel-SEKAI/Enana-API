import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_root():
    """
    Test root endpoint
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Enana Image Generation API is running"}

def test_health_check():
    """
    Test health check endpoint
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_generate_image():
    """
    Test image generation endpoint
    """
    # Simple text widget test
    payload = {
        "widget": {
            "type": "Page",
            "child": {
                "type": "Container",
                "width": 200,
                "height": 100,
                "color": [255, 255, 255, 255],
                "child": {
                    "type": "Text",
                    "text": "Hello, Enana!",
                    "font_size": 16,
                    "color": [0, 0, 0, 255]
                }
            }
        },
        "scale": 1.0
    }
    
    response = client.post("/api/v1/image/generate", json=payload)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    assert len(response.content) > 0

def test_generate_image_with_invalid_json():
    """
    Test image generation with invalid JSON
    """
    # Invalid widget type
    payload = {
        "widget": {
            "type": "InvalidWidgetType",
            "child": {
                "type": "Text",
                "text": "Hello"
            }
        },
        "scale": 1.0
    }
    
    response = client.post("/api/v1/image/generate", json=payload)
    assert response.status_code == 500

def test_generate_image_with_invalid_scale():
    """
    Test image generation with invalid scale
    """
    # Scale too large
    payload = {
        "widget": {
            "type": "Page",
            "child": {
                "type": "Text",
                "text": "Hello"
            }
        },
        "scale": 10.0  # Scale exceeds maximum allowed value
    }
    
    response = client.post("/api/v1/image/generate", json=payload)
    assert response.status_code == 422

def test_generate_image_with_column():
    """
    Test image generation with Column widget
    """
    payload = {
        "widget": {
            "type": "Page",
            "child": {
                "type": "Column",
                "width": 300,
                "height": 200,
                "color": [240, 240, 240, 255],
                "children": [
                    {
                        "type": "Text",
                        "text": "First Line",
                        "font_size": 18,
                        "color": [255, 0, 0, 255]
                    },
                    {
                        "type": "Text",
                        "text": "Second Line",
                        "font_size": 16,
                        "color": [0, 255, 0, 255]
                    },
                    {
                        "type": "Text",
                        "text": "Third Line",
                        "font_size": 14,
                        "color": [0, 0, 255, 255]
                    }
                ]
            }
        },
        "scale": 1.0
    }
    
    response = client.post("/api/v1/image/generate", json=payload)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    assert len(response.content) > 0
