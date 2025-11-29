import requests
import json

# Default API token (should match the one in app/core/config.py)
API_TOKEN = "default_token"

# Test health check endpoint
print("Testing health check endpoint...")
response = requests.get("http://localhost:8000/health")
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
print()

# Test image generation endpoint with valid token
print("Testing image generation endpoint with valid token...")
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

# Add Authorization header with Bearer token
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

response = requests.post("http://localhost:8000/api/v1/image/generate", json=payload, headers=headers)
print(f"Status Code: {response.status_code}")
print(f"Content Type: {response.headers.get('Content-Type', 'N/A')}")
print(f"Content Length: {len(response.content)} bytes")

if response.status_code == 200:
    # Save the image
    with open("output.png", "wb") as f:
        f.write(response.content)
    print("Image saved as output.png")
else:
    print(f"Error: {response.text}")

print()

# Test image generation endpoint with invalid token
print("Testing image generation endpoint with invalid token...")
invalid_headers = {
    "Authorization": "Bearer invalid_token"
}

response = requests.post("http://localhost:8000/api/v1/image/generate", json=payload, headers=invalid_headers)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")

print()

# Test image generation endpoint without token
print("Testing image generation endpoint without token...")
response = requests.post("http://localhost:8000/api/v1/image/generate", json=payload)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
