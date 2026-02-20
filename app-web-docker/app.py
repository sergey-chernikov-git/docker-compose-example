import uvicorn
import logging

from starlette.middleware.cors import CORSMiddleware
from config import Config
from fastapi import FastAPI, Request
from routers import advice_router
from fastapi.templating import Jinja2Templates
from ctx import lifespan

app = FastAPI(lifespan=lifespan)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler(Config.APP_LOG_FILE), logging.StreamHandler()])

logger = logging.getLogger(__name__)

app.include_router(advice_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def render_static(request: Request):
    logger.info(f"User requested {Config.APP_STATIC_INDEX}")
    return templates.TemplateResponse("index.html",
                                      {"request": request, "APP_URL": f"http://{Config.APP_HOST}:{Config.APP_PORT}"})


if __name__ == "__main__":
    uvicorn.run(app, host=Config.APP_HOST, port=Config.APP_PORT)
