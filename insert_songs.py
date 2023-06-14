from pymongo import MongoClient

cluster = "mongodb+srv://ayla:YzA1IQPPHTOIQ4fn@cluster0.ifixfme.mongodb.net/"
client = MongoClient(cluster)

print(client.list_database_names())

db = client.jukebox

print(db.list_collection_names())


data = [
    {
        "title": "Midnight Whispers",
        "artist": "Luna Rivera",
        "album": "Moonlit Serenade",
        "genre": "Jazz Fusion",
        "year": "2022"
    },
    {
        "title": "Electric Dreams",
        "artist": "Neon Skyline",
        "album": "Neon Dreams",
        "genre": "Synthwave",
        "year": "2023"
    },
    {
        "title": "Lost in Translation",
        "artist": "Echoes of Eternity",
        "album": "Echo Chamber",
        "genre": "Progressive Metal",
        "year": "2021"
    },
    {
        "title": "Sunset Boulevard",
        "artist": "Summer Breeze",
        "album": "Coastal Vibes",
        "genre": "Pop",
        "year": "2020"
    },
    {
        "title": "Rhythm of the Rain",
        "artist": "Midnight Storm",
        "album": "Silver Linings",
        "genre": "Indie Folk",
        "year": "2023"
    },
    {
        "title": "City Lights",
        "artist": "Electric Pulse",
        "album": "Neon Nights",
        "genre": "Electronic Dance",
        "year": "2022"
    },
    {
        "title": "Serenade in Blue",
        "artist": "Velvet Harmony",
        "album": "Midnight Sonata",
        "genre": "Jazz",
        "year": "2021"
    },
    {
        "title": "Northern Lights",
        "artist": "Aurora Skies",
        "album": "Celestial Journey",
        "genre": "Ambient",
        "year": "2023"
    },
    {
        "title": "Lost Without You",
        "artist": "Stellar Heights",
        "album": "Starry Eyes",
        "genre": "Pop Rock",
        "year": "2020"
    },
    {
        "title": "Whispers in the Wind",
        "artist": "Solstice Serenade",
        "album": "Enchanted Melodies",
        "genre": "New Age",
        "year": "2022"
    }
]

songs = db.songs

result = songs.insert_many(data)
