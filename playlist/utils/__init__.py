import os


BANNER = "Playlist Manager"

if os.name == "nt":  # pragma: no cover
    # windows can't handle the above charmap
    BANNER = "Playlist Manager"
