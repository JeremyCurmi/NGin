import os


def get_str_env(key: str, default: str = "") -> str:
    return str(os.getenv(key, default))


def get_int_env(key: str, default: int = 0) -> int:
    return int(os.getenv(key, default))
