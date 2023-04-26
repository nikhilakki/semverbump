# Copyright (c) 2023 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import argparse
import json
import subprocess
from typing import Dict, Any, Tuple

try:
    try:
        import tomllib as tomli
    except ModuleNotFoundError:
        import tomli

    from utils import TomlWriter as tw

    has_toml_support = True

    def load_toml(file_name: str) -> Dict[str, Any]:
        with open(file_name, "rb") as f:
            version_data = tomli.load(f)
        return version_data

    def dump_toml(version_data: Dict[str, Any], file_name: str) -> None:
        with open(file_name, "w") as f:
            tw.dumps(version_data, f)

except ModuleNotFoundError:
    has_toml_support = False

try:
    import yaml

    has_yaml_support = True

    def load_yaml(file_name: str) -> Dict[str, Any]:
        with open(file_name, "r") as f:
            version_data = yaml.safe_load(f)
        return version_data

    def dump_yaml(version_data: Dict[str, Any], file_name: str) -> None:
        with open(file_name, "w") as f:
            yaml.safe_dump(version_data, f)

except ModuleNotFoundError:
    has_yaml_support = False


def bump_version(current_version: str, bump_type: str) -> str:
    version_parts = [int(part) for part in current_version.split(".")]
    if bump_type == "major":
        version_parts[0] += 1
        version_parts[1] = 0
        version_parts[2] = 0
    elif bump_type == "minor":
        version_parts[1] += 1
        version_parts[2] = 0
    elif bump_type == "patch":
        version_parts[2] += 1
    new_version = ".".join(str(part) for part in version_parts)
    return new_version


def commit_and_tag(commit_message: str, tag_name: str) -> None:
    # Stage all changes
    subprocess.run(["git", "add", "-A"])

    # Create the commit
    subprocess.run(["git", "commit", "-m", commit_message])

    # Create the tag
    subprocess.run(["git", "tag", "-a", tag_name, "-m", commit_message])


def has_uncommitted_changes() -> bool:
    return (
        subprocess.run(
            ["git", "diff", "--exit-code"], stdout=subprocess.PIPE
        ).returncode
        == 1
    )


def load_json(file_name: str) -> Dict[str, Any]:
    with open(file_name, "r") as f:
        version_data = json.load(f)
    return version_data


def dump_json(version_data: dict, file_name: str) -> None:
    with open(file_name, "w") as f:
        f.write(json.dumps(version_data))


def get_version_from_dict(d: dict, version_path: str) -> str:
    keys = version_path.split(".")
    value = d
    for key in keys:
        value = value[key]
    return str(value)


def run_bump(
    version_data: dict, version_path: str, bump: str
) -> Tuple[Dict[str, Any], str]:
    current_version = get_version_from_dict(version_data, version_path)
    print(f"{current_version=}")
    # Bump the version
    new_version = bump_version(current_version, bump)
    # Update the version in the file
    version_data["version"] = new_version
    # Commit and tag changes

    return version_data, new_version


def main() -> None:
    # Check for uncommitted changes
    # if has_uncommitted_changes():
    #     print("Error: there are uncommitted changes in the repository")
    #     exit(1)

    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Git auto commit and tag with semver version bump"
    )
    parser.add_argument(
        "bump",
        choices=["major", "minor", "patch"],
        help="the type of version bump to perform",
    )

    parser.add_argument(
        "--version-file",
        "-f",
        help="the JSON or TOML file containing the current version",
        default="package.json",
    )
    parser.add_argument(
        "--version-path",
        "-p",
        help="the JSON or TOML file containing the current version",
        default="version",
    )
    args = parser.parse_args()

    file_path = args.version_file
    match file_path.split(".")[-1].lower():
        case "json":
            version_data, new_version = run_bump(
                load_json(file_path), args.version_path, args.bump
            )
            dump_json(version_data, file_path)
            # Load the current version from the file
            # commit_and_tag(f"Version Updated to {new_version}", f"v{new_version}")
        case "toml":
            if has_toml_support:
                print(f"{has_toml_support}")
                version_data, new_version = run_bump(
                    load_toml(file_path), args.version_path, args.bump
                )
                dump_toml(version_data, file_path)
                # Load the current version from the file
                # commit_and_tag(f"Version Updated to {new_version}", f"v{new_version}")
            else:
                print(
                    "Looks like you are not using Py3.11+ run `pip install semverbump[tomli]` to add support for toml files"
                )
        case "yaml" | "yml":
            if has_yaml_support:
                version_data, new_version = run_bump(
                    load_yaml(file_path), args.version_path, args.bump
                )
                dump_yaml(version_data, file_path)
                # Load the current version from the file
                # commit_and_tag(f"Version Updated to {new_version}", f"v{new_version}")
            else:
                print(
                    "Run `pip install semverbump[pyyaml]` to add support for yaml files"
                )
        case _:
            print("Invalid / un-supported file format!")


if __name__ == "__main__":
    main()
