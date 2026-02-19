from fastapi import APIRouter
from config import Config

router = APIRouter(
    prefix=f"{Config.APP_BASE_PATH_V1}"
)


@router.get("/advices")
async def get_advices():
    return "It is not your business"
