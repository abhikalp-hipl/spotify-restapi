# Spotify Playlist Management Script

This project provides a collection of Python scripts that allow you to interact with Spotify's Web API for managing playlists. The functionalities provided include fetching track details from a playlist, adding or removing tracks from a playlist, updating playlist details (such as name or description), and more.

### Features:
1. **Fetch Playlist Tracks** - Retrieve track details from a specific playlist and display them in a DataFrame format.
2. **Add Tracks to Playlist** - Add one or more tracks to an existing playlist.
3. **Remove Tracks from Playlist** - Remove one or more tracks from a playlist.
4. **Update Playlist Details** - Modify the name, description, and visibility (public/private) of a playlist.

### Authentication
For some operations (e.g., adding/removing tracks), you will need to authenticate using OAuth 2.0. The scripts use Authorization Code Flow to get access tokens and interact with Spotify APIs.

To obtain access tokens:

- `Client ID` and `Client Secret` are required, which you can get by registering your application in the Spotify Developer Dashboard.
- You will also need to authorize the app using your Spotify account by visiting a URL that will be provided in the terminal.


### Requirements
- Python 3.x
- `requests` library
- `pandas` library (for track listing)

You can install the necessary dependencies using:
```bash
pip install requests pandas
