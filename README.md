# Billboard Hot 100 → Spotify Playlist Generator

This project automatically creates a Spotify playlist based on the Billboard Hot 100 chart for any date. Enter a date, and the script retrieves that week's chart, matches each track to Spotify, and builds a private playlist in your account.

## Features
- Fetches the Billboard Hot 100 for a specified date
- Searches Spotify and matches each track to its corresponding song
- Automatically creates a private Spotify playlist populated with all matched tracks
- Fully automated workflow using the Spotify Web API

## Technology Overview
- **Python 3**
- **Requests / BeautifulSoup** for Billboard chart scraping  
- **Spotipy (Spotify Web API wrapper)** for playlist creation and track search  
- **dotenv** for environment variable management

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <project-folder> 
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Configure your Spotify credentials
Create a .env file in the project root with:
```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```
You can obtain these by creating a Spotify Developer App.
### 4. Run the script
```bash
python main.py
```
Enter a Billboard chart date (format: YYYY-MM-DD) and the playlist will be generated automatically.
```
Project Structure
main.py          # Core script
README.md        # Project documentation
.gitignore       # Prevents sensitive files from being committed
LICENSE          # Open-source license
```
## Notes

- .env and token.txt are intentionally excluded via .gitignore.

- Spotify authentication requires your own client credentials.

- Playlists are created as private by default.

## License

This project is released under the MIT License.
