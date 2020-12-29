import re

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from playlist.config import settings


class SpotifyService:
    def __init__(self):
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials()
        )
        self.fields = settings.get("spotify.playlist.fields")
        self.track_fields = settings.get("spotify.playlist.track.fields")

    def get_playlist_info(self, playlist):
        self._id_validator(playlist)
        info = None
        if info is None or self.pull:
            info = self.spotify.playlist(
                playlist_id=playlist, fields=self.fields
            )
        return info

    def get_playlist_tracks(self, playlist):
        self._id_validator(playlist)
        tracks = []
        if self.track_fields is not None:
            self.track_fields += ",next,limit,previous,offset,total"

        if len(tracks) == 0:
            results = self.spotify.playlist_items(
                playlist_id=playlist, fields=self.track_fields
            )
            tracks = results["items"]
            while results["next"]:
                results = self.spotify.next(results)
                tracks.extend(results["items"])

        return tracks

    def _id_validator(self, playlist):
        uri_regex = r"spotify:(episode|show|playlist|track|album|artist|user):[a-zA-Z0-9]+"
        id_only_regex = "[a-zA-Z0-9]+"

        if not re.match(uri_regex, playlist) or not re.match(
            id_only_regex, playlist
        ):
            raise ValueError(
                "Invalid Spotify ID reason: value does not match pattern: < '%s' >"
                % uri_regex
            )
