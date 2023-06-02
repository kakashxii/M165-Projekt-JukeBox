import random

class Song:
    def __init__(self, title, artist, album=None, genre=None, year=None, _id=None):
        if(_id is not None):
            self._id = _id
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.year = year

class Jukebox:
    def __init__(self, song):
        self.songs = []
        self.playlist = []

    def add_song(self, song):
        self.songs.append(song)
        print("Song added succesfully. ")
    
    def update_song(self, song):
        for i, s in enumerate(self.songs):
            if s.title == song.title and s.artist == song.artist:
                self.songs[i] = song
                print("Song updated successfully. ")
                return
            print("Song not found. ")

    def deltete_song(self, song):
            if song in self.songs:
                self.songs.remove(song)
                print("Song deleted successfully. ")
            else:
                print("Song not found. ")
    
    def search_songs(self, search_query):
        results = []
        for song in self.songs:
            if(
                search_query.lower() in song.title.lower() or
                search_query.lower() in song.artist.lower() or
                search_query.lower() in song.album.lower() or
                search_query.lower() in song.genre.lower()

            ):
                results.append(song)
        return results
    
    def add_to_playlist(self, song):
        self.playlist.append(song)
        print("Song added to playlist.")
    
    def play_playlist(self):
        if len(self.playlist) > 0:
            for song in self.playlist:
                print("Playing:", song.title, "-", song.artist)
        else:
            random_song = random.choice(self.songs)
            print("No songs in the playlist. Playing a random song:", random_song.title, "-", random_song.artist)


