# Enana Image Generation API

A FastAPI-based backend service for generating images using Enana UI library.

## Features

- **FastAPI Framework**: High-performance, easy-to-use web framework
- **Enana Integration**: Generate images from JSON UI configurations
- **RESTful API**: Well-designed API with Swagger documentation
- **Containerized**: Docker support for easy deployment
- **Logging**: Comprehensive logging for monitoring and debugging
- **CORS Support**: Cross-origin resource sharing enabled
- **Health Check**: Built-in health check endpoint

## Getting Started

### Prerequisites

- Python 3.13 or higher
- uv (Python package manager and virtual environment tool)
- Docker (optional, for containerized deployment)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Parallel-SEKAI/Enana.git
   cd enana_api
   ```

2. **Create and activate virtual environment**
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   uv install
   ```

### Running the Application

#### Development Mode

```bash
uv run start
```

The application will be available at `http://localhost:8000`

#### Docker Deployment

```bash
docker-compose up -d
```

The application will be available at `http://localhost:8000`

## API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## API Endpoints

### POST /api/v1/image/generate

Generate image from JSON configuration.

**Request Body**:
```json
{
  "widget": {
    "type": "Page",
    "child": {
      "type": "Container",
      "width": 400,
      "height": 300,
      "color": [255, 255, 255, 255],
      "child": {
        "type": "Text",
        "text": "Hello, Enana!",
        "font_size": 24,
        "color": [0, 0, 0, 255]
      }
    }
  },
  "scale": 1.0
}
```

**Response**:
- `200 OK`: Returns generated image in PNG format
- `400 Bad Request`: Invalid request parameters
- `500 Internal Server Error`: Error generating image

## Usage Examples

### Using curl

```bash
curl -X POST "http://localhost:8000/api/v1/image/generate" \
  -H "Content-Type: application/json" \
  -d '{"widget": {"type": "Page", "child": {"type": "Text", "text": "Hello"}}, "scale": 1.0}' \
  -o output.png
```

### Using Python requests

```python
import requests
import json

url = "http://localhost:8000/api/v1/image/generate"

payload = {
    "widget": {
        "type": "Page",
        "child": {
            "type": "Container",
            "width": 400,
            "height": 300,
            "color": [255, 255, 255, 255],
            "child": {
                "type": "Text",
                "text": "Hello, Enana!",
                "font_size": 24,
                "color": [0, 0, 0, 255]
            }
        }
    },
    "scale": 1.0
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    with open("output.png", "wb") as f:
        f.write(response.content)
    print("Image generated successfully!")
else:
    print(f"Error: {response.status_code} - {response.text}")
```

## Project Structure

```
enana_api/
├── app/
│   ├── api/              # API routes
│   ├── core/             # Core configuration
│   ├── services/         # Business logic
│   └── schemas/          # Data models
├── tests/                # Test scripts
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── pyproject.toml        # Project dependencies
└── README.md             # This file
```

## Configuration

The application can be configured using environment variables:

- `DEBUG`: Enable/disable debug mode (default: `True`)
- `LOG_LEVEL`: Log level (default: `INFO`)
- `HOST`: Server host (default: `0.0.0.0`)
- `PORT`: Server port (default: `8000`)

## Testing

Run tests using pytest:

```bash
uv run pytest
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
