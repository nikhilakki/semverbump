from src import bump
from src.config import VERSION_FILE_PATH, VERSION_KEY


if __name__ == "__main__":
    if VERSION_FILE_PATH is not None and VERSION_KEY is not None:
        version_object = bump.read_version_file(VERSION_FILE_PATH)
        bump.bump_version(version_object, bump.UpdateType.MINOR)
    else:
        print("Env vars not configured!")
