import requests
from validation import check_access_token, get_new_access_token
from config import ACCESS_TOKEN, REFRESH_TOKEN

def search_album(album_name):
    """
    Search for an album by name and return its ID.
    """
    url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    
    params = {
        "q": album_name,
        "type": "album",
        "limit": 1 
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        albums = data.get('albums', {}).get('items', [])
        if albums:
            album_id = albums[0]['id']
            print(f"Album found: {albums[0]['name']} (ID: {album_id})")
            return album_id
        else:
            print("No albums found.")
            return None
    else:
        print("Error searching for album:", response.json())
        return None

def get_tracks_from_album(album_id):
    """
    Get all tracks from an album using its ID.
    """
    url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        tracks = response.json().get('items', [])
        track_list = []
        
        for track in tracks:
            track_info = {
                'name': track['name'],
                'id': track['id'],
                'duration_ms': track['duration_ms'],
                'preview_url': track['preview_url']
            }
            track_list.append(track_info)
        
        return track_list
    else:
        print("Error retrieving tracks:", response.json())
        return None

if __name__ == "__main__":
    
    if not check_access_token(ACCESS_TOKEN):
        print("Access token is invalid. Refreshing...")
        ACCESS_TOKEN = get_new_access_token(REFRESH_TOKEN)
    
    album_name = input("Enter the name of the album: ")
    
    album_id = search_album(album_name)
    
    if album_id:
        tracks = get_tracks_from_album(album_id)
        
        if tracks:
            print(f"Tracks in '{album_name}':")
            for track in tracks:
                print(f"- {track['name']} (ID: {track['id']}, Duration: {track['duration_ms']} ms)")