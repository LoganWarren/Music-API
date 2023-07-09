import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from secret import client_id, client_secret
from prettytable import PrettyTable
# Set up Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

# Create Spotify client
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Search for a track
search_query = input("Enter the name of the artist or song: ")
results = sp.search(q=search_query, limit=20)
table = PrettyTable(['Track Number', 'Track Name', 'Artist', 'Album', 'Release Date', 'Popularity'])

for i, t in enumerate(results['tracks']['items']):
    track_name = t['name']
    artist = t['artists'][0]['name']
    album = t['album']['name']
    release_date = t['album']['release_date']
    popularity = t['popularity']

    table.add_row([i, track_name, artist, album, release_date, popularity])

print(table)
