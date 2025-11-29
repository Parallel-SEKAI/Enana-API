from typing import Any, Dict

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import Response
from pydantic import BaseModel, Field

from app.core.logger import setup_logger
from app.services.image_generator import generate_image_from_json

logger = setup_logger(__name__)

router = APIRouter()


class ImageGenerationRequest(BaseModel):
    """
    Request model for image generation
    """

    widget: Dict[str, Any] = Field(
        ..., description="JSON configuration for the UI widget"
    )
    scale: float = Field(
        default=1.0, ge=0.1, le=5.0, description="Scale factor for the image"
    )


@router.post("/generate", response_class=Response)
async def generate_image(request: Request, body: ImageGenerationRequest):
    """
    Generate image from JSON configuration

    This endpoint accepts a JSON configuration for a UI widget and generates
    a corresponding image file, returning it as a binary response.

    Args:
        request: FastAPI request object
        body: Image generation request parameters

    Returns:
        Response with generated image in PNG format

    Raises:
        HTTPException: If there's an error generating the image
        HTTPException: If the provided token is invalid
    """
    try:
        logger.info(f"Received image generation request with scale: {body.scale}")

        # Get token from Authorization header
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            raise HTTPException(
                status_code=401, detail="Authorization header is missing"
            )

        # Extract token (remove Bearer prefix if present)
        if auth_header.startswith("Bearer "):
            token = auth_header[7:]
        else:
            token = auth_header

        # Generate image with token validation
        image_bytes = generate_image_from_json(body.widget, body.scale, token)

        logger.info("Image generation completed successfully")

        # Return image as response
        return Response(
            content=image_bytes,
            media_type="image/png",
            headers={"Content-Disposition": "inline; filename=generated_image.png"},
        )
    except ValueError as e:
        logger.error(f"Token validation error: {e}")
        raise HTTPException(status_code=401, detail=str(e))
    except HTTPException:
        # Re-raise HTTP exceptions (they already have proper status codes)
        raise
    except Exception as e:
        logger.error(f"Error generating image: {e}", exc_info=True)
        raise HTTPException(
            status_code=500, detail=f"Failed to generate image: {str(e)}"
        )
