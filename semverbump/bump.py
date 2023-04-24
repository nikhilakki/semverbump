# Copyright (c) 2023 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import argparse
import json
import subprocess
import tomllib


def bump_version(current_version, bump_type):
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


def commit_and_tag(commit_message, tag_name):
    # Stage all changes
    subprocess.run(["git", "add", "-A"])

    # Create the commit
    subprocess.run(["git", "commit", "-m", commit_message])

    # Create the tag
    subprocess.run(["git", "tag", "-a", tag_name, "-m", commit_message])


def has_uncommitted_changes():
    return (
        subprocess.run(
            ["git", "diff", "--exit-code"], stdout=subprocess.PIPE
        ).returncode
        == 1
    )


def load_json(file_name: str):
    with open(file_name, "r") as f:
        version_data = json.load(f)
    return version_data


def load_toml(file_name: str):
    with open(file_name, "rb") as f:
        version_data = tomllib.load(f)
    return version_data


def dump_json(file_name: str):
    with open(file_name, "r") as f:
        version_data = json.dump(f)
    return version_data


def dump_toml(file_name: str):
    with open(file_name, "r") as f:
        version_data = tomllib.dumps(f.write())
    return version_data


def get_version_from_dict(d: dict, version_path: str) -> str:
    keys = version_path.split(".")
    value = d
    for key in keys:
        value = value[key]
    return value


def run_bump(version_data: dict, version_path: str, bump: str):
    current_version = get_version_from_dict(version_data, version_path)
    # Bump the version
    new_version = bump_version(current_version, bump)
    # Update the version in the file
    version_data["version"] = new_version
    # Commit and tag changes
    commit_and_tag(f"Version Updated to {new_version}", f"v{new_version}")
    return version_data


def main():
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
        "-vf",
        help="the JSON or TOML file containing the current version",
        default="package.json",
    )
    parser.add_argument(
        "--version-path",
        "-vp",
        help="the JSON or TOML file containing the current version",
        default="project.version",
    )
    args = parser.parse_args()

    file_path = args.version_file
    match file_path.split(".")[-1].lower():
        case "json":
            version_data = run_bump(load_json(file_path), args.version_path, args.bump)
            dump_json(version_data)
        case "toml":
            print(f"{file_path=}")
            data = load_toml(file_path)
            print(f"{data=}")
            version_data = run_bump(data, args.version_path, args.bump)
            dump_toml(version_data)
        case _:
            print("Invalid format (json or toml supported!)")
    # Load the current version from the file
    print(f"{version_data=}")


if __name__ == "__main__":
    main()
