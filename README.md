# Jukebox Project

This Jukebox project is a school project for Module 165 in the second year. It allows you to manage and play music tracks. The project consists of two main components:

- Management: Add, edit, and delete stored music tracks.
- Player: Search for music tracks, add tracks to a playlist, and play the playlist.

## Prerequisites

- Python 3.x
- MongoDB

## Installation

1. Clone the repository to your local machine:


2. Navigate to the project directory:

```
cd M165-Projekt-Jukebox
```


3. Create a virtual environment:

```
python3 -m venv env
```


4. Activate the virtual environment:

- For Linux/Mac:

  ```
  source env/bin/activate
  ```

- For Windows:

  ```
  .\env\Scripts\activate
  ```

5. Install the required dependencies:

```
pip install -r requirements.txt
```


6. Set up the configuration file:

- Create a `config.yml` file in the project directory.
- Populate the `config.yml` file with the necessary configuration values. For example:

  ```yaml
  DB_HOST: mongodb://localhost:27017/
  DB_NAME: jukebox
  ```

7. Start the application:

```
python main.py config.yml
```


## Usage

- Search songs: Enter a search query to find songs by title, artist, album, or genre.
- Add song: Add a new song to the collection by providing the required details.
- Update song: Update an existing song's details by entering the song ID and providing updated information.
- Delete song: Remove a song from the collection by entering the song ID.
- Add song to playlist: Add a specific song to the playlist for playback.
- Play playlist: Play the songs in the playlist.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your feature or make changes to fix the bug.
4. Commit and push your changes.
5. Submit a pull request.


