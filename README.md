# Spotify API - REST Operations

This project contains a collection of Python scripts that interact with Spotify's Web API, providing features to manage playlists, albums, and tracks. With these scripts, you can fetch details from playlists, add or remove tracks, modify playlist details, manage saved albums, and more.

## Features:
1. **Add Tracks to Playlist** (`add_songs.py`) - Add one or more tracks to an existing playlist.
2. **Remove Tracks from Playlist** (`delete_songs.py`) - Remove one or more tracks from a playlist.
3. **Update Playlist Details** (`change_playlist_details.py`) - Modify the name, description, and visibility (public/private) of a playlist.
4. **Fetch Playlist Details** (`get_playlist_details.py`) - Retrieve details of a specific playlist.
5. **Manage Saved Albums**:
   - **Get Saved Albums** (`get_saved_albums.py`) - Fetch a list of albums saved in your Spotify library.
   - **Save an Album** (`save_album.py`) - Save an album to your Spotify library.
   - **Remove an Album** (`remove_album.py`) - Remove an album from your Spotify library.
6. **Get Tracks from Album** (`get_album_tracks.py`) - Retrieve all tracks from a specific album.
7. **Check Access Tokens** (`get_tokens.py`) - Obtain and refresh authentication tokens for accessing Spotify's Web API.
8. **Album Details** (`check_saved_album.py`) - Fetch and display details of albums in your saved collection.

## Authentication
For certain operations (e.g., adding/removing tracks, updating playlists), authentication is required using OAuth 2.0. The scripts use **Authorization Code Flow** to obtain access tokens, which are necessary to interact with the Spotify APIs.

To obtain access tokens:
- **Client ID** and **Client Secret** are required, which you can get by registering your application in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
- You will also need to authorize the app using your Spotify account. The terminal will provide a URL that you can visit to complete the authorization process.

## Requirements
- Python 3.x
- `requests` library
- `pandas` library (for track listing)

## Environment Variables

You must define the following variables in a `.env` file:

- **`CLIENT_ID`** - Your Spotify application’s Client ID.
- **`CLIENT_SECRET`** - Your Spotify application’s Client Secret.
- **`ACCESS_TOKEN`** - Your access token for Spotify's Web API (generated after authentication).
- **`REFRESH_TOKEN`** - A refresh token to obtain a new access token when the current one expires.


## How to Securely Manage Credentials

**Important**: Ensure that the `.env` file is **not** tracked by version control (e.g., Git). Add the `.env` file to your `.gitignore` to avoid accidentally sharing your credentials.

## Additional Notes:

- **OAuth Tokens**: If you need to refresh your access token, the script will automatically attempt to use the **refresh token** to obtain a new access token when the current one expires.

- **Error Handling**: If an API request fails (e.g., invalid credentials or network issues), the script will display an error message with details to help you troubleshoot.

