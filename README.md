# Billboard → Spotify Time Machine

Generate a Spotify playlist from any Billboard Hot 100 chart with a single command. Choose a date, and the script retrieves that week’s chart, matches each track to Spotify, and creates a private playlist in your account.

## How it looks like in the Terminal Output:
<img width="1766" height="191" alt="image" src="https://github.com/user-attachments/assets/0a1fa67e-01e2-466f-a761-34cdbb36fd0f" />

##  How it looks like in spotify:
<img width="950" height="727" alt="image" src="https://github.com/user-attachments/assets/1abad223-3123-4edc-b6da-bc7fe374554c" />




## Features

- Fetches the official Billboard Hot 100 for any date (1958–present)

- Searches Spotify using track and artist matching for accurate results

- Automatically creates a private playlist titled “Billboard Hot 100 – [Date]”

- Caches lookups to reduce repeated API calls

- Logs any unmatched songs

- Clean, documented Python code using modern best practices

## Tech Stack

- `Python 3.9+`

- `requests` + `BeautifulSoup4` for Billboard scraping

- `spotipy` for Spotify Web API integration

- `python-dotenv` for secure credential handling

## Setup
### 1. Clone the repository
```bash
git clone https://github.com/alyasa-dev/Billboard-to-spotify.git
cd Billboard-to-spotify
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Add your Spotify API credentials

Create a `.env` file in the project root:
```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
YOUR_REDIRECT_URI = "http://127.0.0.1:8080/callback"
```
### 4. Run the script
```bash
python main.py
```

Enter a date in the format `YYYY-MM-DD` and the playlist will be created.

### Project Structure
```
.
├── main.py          # Core script
├── README.md        # Project documentation
├── requirements.txt # Dependencies
├── LICENSE          # MIT License
├── .gitignore       # Excludes environment and token files
└── .env.example     # template for environment variables
```
Notes

- `.env` and `token.txt` are intentionally ignored by Git for security.

- Spotify authentication requires your own developer credentials.

- Playlists are private by default.

## License

This project is licensed under the [MIT License](LICENSE).
