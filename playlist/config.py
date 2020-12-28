from pathlib import Path

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    root_path="{}/.playlist/".format(str(Path.home())),
    settings_files=["settings.toml", ".secrets.toml"],
)
