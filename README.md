🎵 Billboard → Spotify Playlist Maker

This little Python script takes a Billboard Hot 100 chart from any date you choose and automatically creates a matching Spotify playlist for you.
Yes, it’s basically a time machine but for vibes.

💡 What it does

You enter a date (like 2010-05-20)

It scrapes the Billboard Hot 100 songs from that week

It searches Spotify for each song

It creates a private Spotify playlist with those songs

Boom. Nostalgia playlist.

🚀 How to use it

1. Clone or download the repo
2. Install the requirements:
<pre>pip install -r requirements.txt # Run the main script python main.py  </pre>
3. Create a .env file (this stays private on your machine!)
Add your Spotify info:
<pre>SPOTIFY_CLIENT_ID=your_id_here
SPOTIFY_CLIENT_SECRET=your_secret_here</pre>
4. Run it:
<pre>python main.py</pre>
5. Enter a date and watch Spotify do its magic.
⚠️ Important

Don’t upload your .env or token.txt — they’re in .gitignore already.

This script won’t run unless you create your own Spotify dev app and put the keys in your .env.

📁 Files in the repo

main.py — the whole project

.gitignore — keeps your secrets safe

README.md — this file

LICENSE — standard open-source license


