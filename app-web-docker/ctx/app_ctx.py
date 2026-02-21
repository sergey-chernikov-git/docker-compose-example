from logging import getLogger
from contextlib import asynccontextmanager

from fastapi import FastAPI

from cache import redis_cache
from config import Config

logger = getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("== App enter lifespan ==")
    logger.info(f"REDIS {Config.RI_APP_HOST}:{Config.RI_APP_PORT} loading...")
    logger.info("REDIS ping...")
    ping = await redis_cache.ping()
    if not ping:
        logger.error("Failed to connect to Redis server at localhost:6379")
        raise ConnectionError(f"Could not connect to Redis server at {Config.RI_APP_HOST}:{Config.RI_APP_PORT}")
    logger.info("Load advices to REDIS...")
    with open("content/advices.txt", "r", encoding="utf-8") as f:
        for idx, line in enumerate(f.readlines()):
            await redis_cache.add(idx line)
    logger.info("== App started ==")
    yield
    logger.info("App exit lifespan")
