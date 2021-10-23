import spotipy
from spotipy.oauth2 import SpotifyOAuth

ID = "Your ID"
SECRET = "Your Secret code"


class Spoti:

    def __init__(self, songs, date):
        self.songs = songs
        self.date = date
        self.song_uris = []
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=ID,
                                                            client_secret=SECRET,
                                                            redirect_uri="http://example.com",
                                                            scope="playlist-modify-private"))
        self.user_id = self.sp.current_user()["id"]

    def search_sp(self):

        for song in self.songs:
            result = self.sp.search(q=song, type="track")
            print(result)

            try:
                uri = result["tracks"]["items"][0]["uri"]
                self.song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")

    def add_tracks(self):
        playlist = self.sp.user_playlist_create(user=self.user_id, name=f"{self.date} TOP 100", public=False)

        self.sp.playlist_add_items(playlist_id=playlist["id"], items=self.song_uris)
