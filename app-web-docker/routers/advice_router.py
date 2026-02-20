from random import random

from fastapi import APIRouter

from cache import redis_cache
from config import Config

router = APIRouter(
    prefix=f"{Config.APP_BASE_PATH_V1}"
)


@router.get("/advices")
async def get_advices():
    advice = await redis_cache.get(10)
    if not advice:
        raise Exception("No advice found")
    return advice
