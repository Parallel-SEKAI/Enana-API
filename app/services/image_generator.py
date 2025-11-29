import tempfile
from pathlib import Path
from typing import Any, Dict

from enana.page import Page

from app.core.config import settings
from app.core.logger import setup_logger

logger = setup_logger(__name__)


def generate_image_from_json(
    widget_json: Dict[str, Any], scale: float = 1.0, token: str = None
) -> bytes:
    """
    Generate image from JSON configuration

    Args:
        widget_json: JSON configuration for the UI widget
        scale: Scale factor for the image
        token: API token for authentication

    Returns:
        Generated image as bytes

    Raises:
        ValueError: If the provided token is invalid
        Exception: If there's an error generating the image
    """
    try:
        # Validate token
        if token != settings.API_TOKEN:
            logger.error(f"Invalid token provided: {token}")
            raise ValueError("Invalid API token")

        # Create Page object from JSON
        logger.debug("Creating Page object from JSON")
        page = Page.from_json(widget_json)

        # Generate image in memory
        logger.debug("Generating image")

        # Use tempfile to save the image temporarily
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_path = Path(temp_file.name)

        try:
            # Paint the page to the temporary file
            page.paint(scale=scale, filename=temp_path)

            # Read the image bytes
            with open(temp_path, "rb") as f:
                image_bytes = f.read()
        finally:
            # Clean up temporary file
            temp_path.unlink()

        logger.debug(f"Image generated successfully, size: {len(image_bytes)} bytes")
        return image_bytes
    except ValueError as e:
        logger.error(f"Token validation error: {e}")
        raise
    except Exception as e:
        logger.error(f"Error in generate_image_from_json: {e}", exc_info=True)
        raise
