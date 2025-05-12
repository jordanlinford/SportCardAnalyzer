from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging
import traceback

# Logging setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize Firebase (only once in the app lifecycle)
try:
    logger.debug("Initializing Firebase...")
    from utils.auth import verify_token  # This will initialize Firebase
    logger.debug("Importing card routes...")
    from card_routes import router as card_router
    logger.debug("All imports successful")
except Exception as e:
    logger.error(f"Import error: {str(e)}")
    raise

app = FastAPI(title="Sports Card Market Analysis API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
logger.debug("Including routers...")
app.include_router(card_router)
logger.debug("Router included successfully")

@app.get("/")
async def root():
    try:
        logger.debug("Root endpoint hit")
        return {"message": "Sports Card Market Analysis API"}
    except Exception as e:
        logger.error(f"Error in root: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
