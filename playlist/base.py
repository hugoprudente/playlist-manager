# import re
# import sys
# import os
# import time
# import errno
# from datetime import datetime, timedelta
# from termcolor import colored
from playlist.inventories.json_inventory import JSONInventory
from playlist.services.spotify_service import SpotifyService


class PlaylistGenerator(object):
    def __init__(self, **kwargs):
        self.value = ""
        self.type = kwargs.get("type")
        self.playlist = kwargs.get("playlist")
        self.service = kwargs.get("service")
        self.file = kwargs.get("file")
        self.format = kwargs.get("format")
        self.fields = kwargs.get("fields")

    def upsert_inventory(self):
        if self.service == "spotify":
            spotify = SpotifyService()
            playlist_info = spotify.get_playlist_info(self.playlist)
            playlist_tracks = spotify.get_playlist_tracks(self.playlist)

        if self.type == "json":
            export = JSONInventory()
            if self.file is not None:
                export.writefile(
                    self.file,
                    playlist_tracks,
                    playlist_info,
                    self.fields,
                    self.format,
                )
            else:
                export.stdout(
                    playlist_tracks, playlist_info, self.fields, self.format
                )
