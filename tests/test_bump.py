# import sys

# sys.path.append(sys.path[0] + "/..")
import os
from semverbump import bump

JSON_FILE = os.path.join("tests", "sample.json")
TOML_FILE = os.path.join("tests", "sample.toml")


def test_file_loader_json() -> None:
    assert type(bump._file_loader(JSON_FILE)) == str


def test_file_loader_toml() -> None:
    assert type(bump._file_loader(TOML_FILE)) == str


def test_read_version_file_json() -> None:
    assert type(bump.read_version_file(JSON_FILE)) == dict


def test_read_version_file_toml() -> None:
    assert type(bump.read_version_file(TOML_FILE)) == dict


def test_read_version_file_invalid() -> None:
    assert bump.read_version_file("invalid.md") is None


def test_bump_helper_major() -> None:
    assert bump.update_version(["0", "1", "1"], bump.UpdateType.MAJOR) == [
        "1",
        "0",
        "0",
    ]


def test_bump_helper_minor() -> None:
    assert bump.update_version(["0", "9", "1"], bump.UpdateType.MINOR) == [
        "0",
        "10",
        "0",
    ]


def test_bump_helper_patch() -> None:
    assert bump.update_version(["0", "1", "9"], bump.UpdateType.PATCH) == [
        "0",
        "1",
        "10",
    ]


def test_bump_version() -> None:
    version_object = {"version": "1.0.0"}
    assert bump.bump_version(
        version_object, bump.UpdateType.MINOR, write_to_disk=False
    ) == {"version": "1.1.0"}


def test_bump_version_write_to_file() -> None:
    version_object = {"version": "1.0.0"}
    assert (
        bump.bump_version(version_object, bump.UpdateType.MINOR, write_to_disk=True)
        is None
    )


def test_write_to_file() -> None:
    assert bump.write_to_file({"version": "1.2.9"}, "sample.json") is None
