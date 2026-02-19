import os

class Config:
    APP_PORT = int(os.environ.get("APP_PORT", "9000"))
    APP_HOST = os.environ.get("APP_HOST", "0.0.0.0")
    APP_LOG_FILE = "data/app-web-docker.log"
    APP_BASE_PATH_V1 = "/api/v1"
    APP_STATIC_INDEX = "static/index.html"
