import json
import tomllib
from enum import Enum
from typing import Union
from src.config import VERSION_FILE_PATH, VERSION_KEY


class UpdateType(Enum):
    MAJOR = 0
    MINOR = 1
    PATCH = 2


def _file_loader(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        version_file = f.read()
    return version_file


def read_version_file(file_path: str) -> dict | None:
    version_file_ext = file_path.split(".")[-1].lower()
    match version_file_ext:
        case "json":
            return json.loads(_file_loader(file_path))
        case "toml":
            return tomllib.loads(_file_loader(file_path))
        case _:
            print("File type not supported")
            return None


def update_version(sem_ver_split: list[str], update_type: UpdateType) -> list[str]:
    final_version = sem_ver_split
    match update_type:
        case UpdateType.MAJOR:
            bumpy = int(sem_ver_split[UpdateType.MAJOR.value])
            final_version[UpdateType.MAJOR.value] = str(bumpy + 1)
            final_version[UpdateType.MINOR.value] = "0"
            final_version[UpdateType.PATCH.value] = "0"

        case UpdateType.MINOR:
            bumpy = int(sem_ver_split[UpdateType.MINOR.value])
            final_version[UpdateType.MINOR.value] = str(bumpy + 1)
            final_version[UpdateType.PATCH.value] = "0"

        case update_type.PATCH:
            bumpy = int(sem_ver_split[UpdateType.PATCH.value])
            final_version[UpdateType.PATCH.value] = str(bumpy + 1)

    return final_version


def bump_version(
    version_object: dict, update_type: UpdateType, write_to_disk: bool = True
) -> Union[dict, None]:
    version = version_object[VERSION_KEY]
    sem_ver_split = version.split(".")
    final_version = ".".join(update_version(sem_ver_split, update_type))
    print(f"{version=} {final_version=}")
    version_object[VERSION_KEY] = final_version
    if write_to_disk:
        write_to_file(version_object, VERSION_FILE_PATH)
    else:
        return version_object


def write_to_file(version_object: dict, file_path: str) -> None:
    with open(file_path, "w") as f:
        f.write(json.dumps(version_object))
