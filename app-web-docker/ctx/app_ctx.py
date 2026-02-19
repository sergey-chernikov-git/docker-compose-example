import os
from contextlib import asynccontextmanager
from logging import getLogger

from fastapi import FastAPI

from config import Config

logger = getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("App enter lifespan")
    # with open("content/advices.txt", "r", encoding="utf-8") as f:
    #     for line in f.readlines():
    #         print(line)
    yield
    # os.remove(Config.APP_LOG_FILE)
    logger.info("App exit lifespan")

