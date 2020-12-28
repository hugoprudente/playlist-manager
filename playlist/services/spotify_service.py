import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from playlist.config import settings


class Spotify:
    def __init__(self):
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials()
        )
        self.fields = settings.get("spotify.playlist.fields")
        self.track_fields = settings.get("spotify.playlist.track.fields")

    def get_playlist_info(self, playlist):
        info = None
        if info is None or self.pull:
            info = self.spotify.playlist(
                playlist_id=playlist, fields=self.fields
            )
        return info

    def get_playlist_tracks(self, playlist):
        tracks = []
        if len(tracks) == 0:
            self.spotify.playlist_items(
                playlist_id=playlist, fields=self.track_fields
            )
        #            tracks = results["items"]
        #            print(results)
        #            while results["next"]:
        #                results = self.spotify.next(results)
        #                print(results)
        #                tracks.extend(results["items"])
        #        print(len(tracks))
        return tracks
