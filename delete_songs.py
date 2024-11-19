import requests
from validation import check_access_token, get_new_access_token
from config import ACCESS_TOKEN, REFRESH_TOKEN

def get_playlist_id(playlist_name, access_token):
    """
    Get the ID of a playlist by its name.
    """
    url = "https://api.spotify.com/v1/me/playlists"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        playlists = response.json().get('items', [])
        for playlist in playlists:
            if playlist['name'].lower() == playlist_name.lower():
                print(f"Playlist found: {playlist['name']} (ID: {playlist['id']})")
                return playlist['id']
        print("Playlist not found.")
        return None
    else:
        print("Error retrieving playlists:", response.json())
        return None

def search_track(track_name, access_token):
    """
    Search for a track by name and return its URI.
    """
    url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    params = {
        "q": track_name,
        "type": "track",
        "limit": 1  
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        tracks = data.get('tracks', {}).get('items', [])
        if tracks:
            track_uri = tracks[0]['uri']
            print(f"Track found: {tracks[0]['name']} (URI: {track_uri})")
            return track_uri
        else:
            print("Track not found.")
            return None
    else:
        print("Error searching for track:", response.json())
        return None

def remove_track_from_playlist(playlist_id, track_uri, access_token):
    """
    Remove a track from a specified playlist using its ID and track URI.
    """
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    data = {
        "tracks": [{"uri": track_uri}] 
    }

    response = requests.delete(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Track removed successfully!")
        print("Response:", response.json())
        return True
    else:
        print(f"Failed to remove track. Status code: {response.status_code}")
        print("Response:", response.json())
        return False

if __name__ == "__main__":
    
    if not check_access_token(ACCESS_TOKEN):
        print("Access token is invalid. Refreshing...")
        ACCESS_TOKEN = get_new_access_token(REFRESH_TOKEN)
    
    playlist_name = input("Enter the name of the playlist you want to remove a song from: ")
    
    playlist_id = get_playlist_id(playlist_name, ACCESS_TOKEN)
    
    if playlist_id:
        track_name = input("Enter the name of the song you want to remove: ")
        
        track_uri = search_track(track_name, ACCESS_TOKEN)
        
        if track_uri:
            remove_track_from_playlist(playlist_id, track_uri, ACCESS_TOKEN)