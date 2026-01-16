from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import your API routers
from app.api.product_api import router as product_router
from app.api.ai_query_api import router as ai_router

# Create FastAPI app instance
app = FastAPI(
    title="Backend API App",
    description="FastAPI backend with Snowflake + AI multi-agent",
    version="1.0.0",
)

# Enable CORS for frontend (adjust allow_origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(product_router, prefix="/api", tags=["Product"])
app.include_router(ai_router, prefix="/api", tags=["AI Query"])

# Optional: health check endpoint
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "Backend is running"}

# Optional: startup event log
@app.on_event("startup")
async def startup_event():
    print("🚀 FastAPI backend started successfully")
