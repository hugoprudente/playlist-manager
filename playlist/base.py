# import re
# import sys
# import os
# import time
# import errno
# from datetime import datetime, timedelta
# from termcolor import colored
from playlist.services.spotify_service import Spotify


class PlaylistGenerator(object):
    def __init__(self, **kwargs):
        self.value = ""
        self.format = kwargs.get("format")
        self.playlist = kwargs.get("playlist")
        self.service = kwargs.get("service")

    def upsert_inventory(self):
        if self.service == "spotify":
            spotify = Spotify()
            #            playlist_info = spotify.get_playlist_info(self.playlist)
            playlist_tracks = spotify.get_playlist_tracks(self.playlist)

        if self.format == "json":
            for x in playlist_tracks:
                x
