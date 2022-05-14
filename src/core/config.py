from dotenv import load_dotenv
from pydantic import BaseSettings

from src.utils import utils


load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str = "NGin"
    API_URL: str = "/api/v1"
    DATABASE_URL: str = utils.get_str_env("DATABASE_URL")
