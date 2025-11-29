from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import image
from app.core.logger import setup_logger

# Setup logger
logger = setup_logger()

# Create FastAPI app
app = FastAPI(
    title="Enana Image Generation API",
    description="A FastAPI-based backend service for generating images using Enana UI library",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development, restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(image.router, prefix="/api/v1/image", tags=["image"])


@app.get("/")
async def root():
    """
    Root endpoint
    """
    return {"message": "Enana Image Generation API is running"}


@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy"}
