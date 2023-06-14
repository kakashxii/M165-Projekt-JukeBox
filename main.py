import random
from pymongo import MongoClient
import sys
import os
import yaml


class Song:
    def __init__(self, title, artist, album=None, genre=None, year=None, _id=None):
        if _id is not None:
            self._id = _id
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.year = year

class Jukebox:
    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)
        self.db = self.client.jukebox
        self.songs = []
        self.playlist = []

    def load_songs_from_database(self):
        songs_collection = self.db.songs
        songs_data = songs_collection.find()
        for song_data in songs_data:
            song = Song(
                song_data['title'],
                song_data['artist'],
                song_data.get('album'),
                song_data.get('genre'),
                song_data.get('year'),
                song_data.get('_id')
            )
            self.songs.append(song)

    def add_song(self, song):
        songs_collection = self.db.songs
        song_data = {
            'title': song.title,
            'artist': song.artist,
            'album': song.album,
            'genre': song.genre,
            'year': song.year
        }
        result = songs_collection.insert_one(song_data)
        song._id = result.inserted_id
        self.songs.append(song)
        print("Song added successfully.")

    def update_song(self, song_id):
        songs_collection = self.db.songs
        for song in self.songs:
            if song._id == song_id:
                updated_title = input(f"Enter updated title (or press Enter to keep the same: {song.title}): ")
                updated_artist = input(f"Enter updated artist (or press Enter to keep the same: {song.artist}): ")
                updated_album = input(f"Enter updated album (or press Enter to keep the same: {song.album}): ")
                updated_genre = input(f"Enter updated genre (or press Enter to keep the same: {song.genre}): ")
                updated_year = input(f"Enter updated year (or press Enter to keep the same: {song.year}): ")

                if updated_title:
                    song.title = updated_title
                if updated_artist:
                    song.artist = updated_artist
                if updated_album:
                    song.album = updated_album
                if updated_genre:
                    song.genre = updated_genre
                if updated_year:
                    song.year = updated_year

                songs_collection.update_one(
                    {'_id': song._id},
                    {
                        '$set': {
                            'title': song.title,
                            'artist': song.artist,
                            'album': song.album,
                            'genre': song.genre,
                            'year': song.year
                        }
                    }
                )
                print("Song updated successfully.")
                return
        print("Song not found.")

    def delete_song(self, song_id):
        songs_collection = self.db.songs
        for song in self.songs:
            if song._id == song_id:
                songs_collection.delete_one({'_id': song._id})
                self.songs.remove(song)
                print("Song deleted successfully.")
                return
        print("Song not found.")

    def search_songs(self, search_query):
        results = []
        for song in self.songs:
            if (
                search_query.lower() in song.title.lower() or
                search_query.lower() in song.artist.lower() or
                (song.album and search_query.lower() in song.album.lower()) or
                (song.genre and search_query.lower() in song.genre.lower())
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

def main():
    prog = sys.argv[0].split('/')[-1]
    if len(sys.argv) < 2:
        print(f'usage: {prog} [configfile]', file=sys.stderr)
        sys.exit(1)

    config_file_path = sys.argv[1]
    if not os.path.exists(config_file_path):
        raise ValueError(f'config file at "{config_file_path}" missing')

    with open(config_file_path, 'r') as f:
        content = f.read()

    config = yaml.load(content, Loader=yaml.SafeLoader)
    assert 'MONGODB_CONNECTION_STRING' in config

    connection_string = config['MONGODB_CONNECTION_STRING']
    jukebox = Jukebox(connection_string)
    jukebox.load_songs_from_database()

    while True:
        print("\n--- Jukebox Menu ---")
        print("1. Search songs")
        print("2. Add song")
        print("3. Update song")
        print("4. Delete song")
        print("5. Add song to playlist")
        print("6. Play playlist")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "0":
            break

        elif choice == "1":
            search_query = input("Enter search query: ")
            search_results = jukebox.search_songs(search_query)
            if len(search_results) > 0:
                print("Search Results:")
                for song in search_results:
                    print(song.title, "-", song.artist)
            else:
                print("No songs found.")

        elif choice == "2":
            title = input("Enter song title: ")
            artist = input("Enter artist name: ")
            album = input("Enter album name (optional): ")
            genre = input("Enter genre (optional): ")
            year = input("Enter year (optional): ")
            song = Song(title, artist, album, genre, year)
            jukebox.add_song(song)

        elif choice == "3":
            song_id = input("Enter song ID: ")
            jukebox.update_song(song_id)

        elif choice == "4":
            song_id = input("Enter song ID: ")
            jukebox.delete_song(song_id)

        elif choice == "5":
            song_id = input("Enter song ID: ")
            for song in jukebox.songs:
                if song._id == song_id:
                    jukebox.add_to_playlist(song)
                    break
            else:
                print("Song not found.")

        elif choice == "6":
            jukebox.play_playlist()

        else:
            print("Invalid choice. Please try again.")

    print("Goodbye!")

if __name__ == '__main__':
    main()
