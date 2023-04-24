# Copyright (c) 2023 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import argparse
import json
import subprocess


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


def main():
    # Check for uncommitted changes
    if has_uncommitted_changes():
        print("Error: there are uncommitted changes in the repository")
        exit(1)

    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Git auto commit and tag with semver version bump"
    )
    parser.add_argument(
        "bump",
        choices=["major", "minor", "patch"],
        help="the type of version bump to perform",
    )
    parser.add_argument("message", help="the commit message")
    parser.add_argument("tag", help="the tag name")
    parser.add_argument(
        "--version-file",
        help="the JSON or TOML file containing the current version",
        default="version.json",
    )
    args = parser.parse_args()

    # Load the current version from the file
    with open(args.version_file, "r") as f:
        version_data = json.load(f)
    current_version = version_data["version"]

    # Bump the version
    new_version = bump_version(current_version, args.bump)

    # Update the version in the file
    version_data["version"] = new_version
    with open(args.version_file, "w") as f:
        json.dump(version_data, f, indent=4)

    # Commit and tag changes
    commit_and_tag(args.message, args.tag)


if __name__ == "__main__":
    main()
