import logging

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import root, sample
from util.env import get_env

# logger config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

# get environment mode
env_mode = get_env("ENV_MODE", "development")

# production時，docsを表示しない
app_params = {}
if env_mode == "production":
    app_params["docs_url"] = None
    app_params["redoc_url"] = None
    app_params["openapi_url"] = None

# create app
app = FastAPI(**app_params)

# mount static folder
app.mount("/static", StaticFiles(directory="/app/static"), name="static")

# add routers
app.include_router(
    root.router
)
app.include_router(
    sample.router
)
