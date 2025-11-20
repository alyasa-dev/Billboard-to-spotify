import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Spotify credentials from .env
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "http://127.0.0.1:8080/callback"
SCOPE = "playlist-modify-private"

# Ask for date input
date = input("Which date do you want to travel to? (YYYY-MM-DD): ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

# Scrape Billboard Hot 100
headers = {
    "USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

song_tags = soup.select("li.o-chart-results-list__item h3.c-title")
songs = [song.get_text(strip=True) for song in song_tags]

# Authenticate with Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

# Search for song URIs
song_uris = []
for song in songs:
    try:
        result = sp.search(q=f"track:{song}", type="track", limit=1)
        items = result['tracks']['items']
        if items:
            song_uris.append(items[0]['uri'])
        else:
            print(f"Song not found on Spotify: {song}")
    except Exception as e:
        print(f"Error searching for {song}: {e}")

# Create playlist
playlist_name = f"{date} Billboard 100"
playlist = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
    description=f"Top 100 Billboard songs from {date}"
)

# Add songs
sp.playlist_add_items(playlist['id'], song_uris)
print(f"Playlist '{playlist_name}' created with {len(song_uris)} songs!")
