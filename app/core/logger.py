import logging
import sys
from typing import Optional

from app.core.config import settings


def setup_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Setup logger with specified name

    Args:
        name: Logger name

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)

    # Check if logger already has handlers to avoid duplicate logs
    if not logger.handlers:
        # Set log level
        logger.setLevel(getattr(logging, settings.LOG_LEVEL.upper()))

        # Create formatter
        formatter = logging.Formatter(settings.LOG_FORMAT)

        # Create console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)

        # Add handler to logger
        logger.addHandler(console_handler)

        # Prevent propagation to root logger
        logger.propagate = False

    return logger
