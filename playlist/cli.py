import argparse
import os
import sys
from pathlib import Path

from playlist.base import PlaylistGenerator
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

    parser = argparse.ArgumentParser(usage="%(prog)s [ spotify | inventory ]")

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s " + read_file_in_root_directory("VERSION"),
    )

    subparsers = parser.add_subparsers()

    # service
    svc_parser = subparsers.add_parser("service", description="service")
    svc_parser.set_defaults(func="")

    # inventory
    arc_parser = subparsers.add_parser(
        "inventory", description="upsert inventory for a given playlist"
    )
    arc_parser.set_defaults(func="upsert_inventory")

    # inventory required
    arc_required = arc_parser.add_argument_group("required arguments")
    arc_required.add_argument(
        "playlist", type=str, nargs="?", help="playlist id"
    )

    # inventory opotional
    arc_parser.add_argument(
        "-s",
        "--service",
        action="store",
        choices=["spotify"],
        default=settings.get("inventory.service")
        if settings.get("inventory.service")
        else "spotify",
    )

    arc_parser.add_argument(
        "-t",
        "--type",
        action="store",
        dest="type",
        default=settings.get("inventory.type")
        if settings.get("inventory.type")
        else "json",
        choices=["googlesheet", "json", "value"],
        help="type of inventory",
    )

    arc_parser.add_argument(
        "-f",
        "--format",
        action="store",
        dest="format",
        default=settings.get("inventory.format")
        if settings.get("inventory.format")
        else "",
        help="output pretty-printed",
    )

    # Parse input
    options, args = parser.parse_known_args(argv)

    try:
        logs = PlaylistGenerator(**vars(options))
        if not hasattr(options, "func"):
            parser.print_help()
            return 1
        getattr(logs, options.func)()
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
