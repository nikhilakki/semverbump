import os

CONFIG = {
    "VERSION_FILE_PATH": os.getenv("VERSION_FILE_PATH", ""),
    "VERSION_KEY": os.getenv("VERSION_KEY", "version"),
}

VERSION_FILE_PATH = CONFIG.get("VERSION_FILE_PATH", "")
VERSION_KEY = CONFIG.get("VERSION_KEY")
