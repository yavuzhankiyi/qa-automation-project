import os
from pathlib import Path

from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parent.parent

ENV_FILE = ROOT_DIR / ".env"

load_dotenv(ENV_FILE)


BASE_URL = os.getenv(
    "BASE_URL",
    "https://www.saucedemo.com"
)

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "https://jsonplaceholder.typicode.com"
)

TEST_USERNAME = os.getenv(
    "TEST_USERNAME",
    "standard_user"
)

TEST_PASSWORD = os.getenv(
    "TEST_PASSWORD",
    "secret_sauce"
)
