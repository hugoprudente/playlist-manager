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
        "--playlist",
        type=str,
        nargs="?",
        help="service playlist id",
        required=True,
    )

    # inventory opotional
    arc_parser.add_argument(
        "--service",
        action="store",
        choices=["spotify"],
        default=settings.get("inventory.service")
        if settings.get("inventory.service")
        else "spotify",
        help="supported service name",
    )

    arc_parser.add_argument(
        "--type",
        action="store",
        dest="type",
        default=settings.get("inventory.type")
        if settings.get("inventory.type")
        else "json",
        choices=["googlesheet", "json", "value"],
        help="inventory storage type",
    )

    arc_parser.add_argument(
        "--format",
        action="store",
        dest="format",
        default=settings.get("inventory.format")
        if settings.get("inventory.format")
        else "",
        help="output format using python format syntax",
    )

    arc_parser.add_argument(
        "--output",
        action="store",
        dest="output",
        default=settings.get("inventory.output")
        if settings.get("inventory.output")
        else "",
        help="output filename or abspath filename",
    )

    arc_parser.add_argument(
        "--fields",
        action="store",
        dest="fields",
        default=settings.get("inventory.fields")
        if settings.get("inventory.fields")
        else "",
        help="jmespath fields query for the output",
    )

    arc_parser.add_argument(
        "--service-fields",
        action="store",
        dest="service_fields",
        default=settings.get("inventory.service_fields")
        if settings.get("inventory.service_fields")
        else "",
        help="service fields fields for the query",
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
