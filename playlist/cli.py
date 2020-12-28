import argparse
import os
import sys
from pathlib import Path

from termcolor import colored

from playlist.config import settings
from playlist.utils.files import read_file


CWD = Path.cwd()


def read_file_in_root_directory(*names, **kwargs):
    """Read a file on root dir."""
    return read_file(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf-8"),
    )


def main(argv=None):

    argv = (argv or sys.argv)[1:]

    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument(
        "--debug",
        default=False,
        required=False,
        action="store_true",
        dest="debug",
        help="Enable debug logs",
    )
    print(settings.default.FOO)

    # print(settings)
    main_parser = argparse.ArgumentParser()

    # services
    svc_subparsers = main_parser.add_subparsers(title="Service", dest="svc")

    # databases

    # cache

    # Parse input
    options, args = main_parser.parse_known_args(argv)

    try:
        print("things")
        # things
    except Exception:
        import platform
        import traceback

        options = vars(options)

        issue_info = "\n".join(
            (
                "Version:       {0}".format(
                    read_file_in_root_directory("VERSION")
                ),
                "Python:        {0}".format(sys.version),
                "Platform:      {0}".format(platform.platform()),
                "Args:          {0}".format(sys.argv),
                "Config: {0}".format(options),
                "",
                traceback.format_exc(),
            )
        )
        sys.stderr.write(issue_info + "\n")
        return 1

    return 0


if __name__ == "__main__":  # pragma: no cover
    main()
