import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from secret import client_id, client_secret

# Set up Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

# Create Spotify client
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Search for a track
search_query = input("Enter the name of the artist or song: ")
results = sp.search(q=search_query, limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])
