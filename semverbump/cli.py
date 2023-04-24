import argparse
from semverbump.bump import bump_version, UpdateType, read_version_file
from semverbump.config import VERSION_FILE_PATH, VERSION_KEY


def main():
    # create an instance of the ArgumentParser class
    parser = argparse.ArgumentParser(description="A CLI for Version Auto Bump")

    # add arguments to the parser
    parser.add_argument(
        "command",
        type=str,
        default="patch",
        help="SemVer pattern - MAJOR|MINOR|PATCH [default: PATCH]",
    )
    # parse the arguments
    args = parser.parse_args()
    if VERSION_FILE_PATH is not None and VERSION_KEY is not None:
        version_object = read_version_file(VERSION_FILE_PATH)
        match str(args.command).lower():
            case "major":
                bump_version(version_object, UpdateType.MAJOR)
            case "minor":
                bump_version(version_object, UpdateType.MINOR)
            case "patch":
                bump_version(version_object, UpdateType.PATCH)
            case _:
                print("Invalid command!! Choose from MAJOR|MINOR|PATCH")
    else:
        print("Env vars not configured!")


if __name__ == "__main__":
    main()
