import os


DEFAULT_BASE_URL = "http://localhost:8080"


def get_base_url() -> str:
    return os.getenv("API_BASE_URL", DEFAULT_BASE_URL).rstrip("/")
