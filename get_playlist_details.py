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

def get_playlist_tracks(playlist_id, access_token):
    """
    Get all tracks from a specified playlist using its ID.
    """
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    tracks = []
    
    while True:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])
            tracks.extend(items)
            if data['next']:
                url = data['next']  
            else:
                break
        else:
            print("Error retrieving tracks:", response.json())
            return None
    
    return tracks

if __name__ == "__main__":
    
    if not check_access_token(ACCESS_TOKEN):
        print("Access token is invalid. Refreshing...")
        ACCESS_TOKEN = get_new_access_token(REFRESH_TOKEN)
    
    playlist_name = input("Enter the name of the playlist you want to retrieve details for: ")
    
    playlist_id = get_playlist_id(playlist_name, ACCESS_TOKEN)
    
    if playlist_id:
        tracks = get_playlist_tracks(playlist_id, ACCESS_TOKEN)
        
        if tracks:
            print(f"\nTracks in '{playlist_name}':")
            for item in tracks:
                track_info = item['track']
                if track_info is not None:  
                    track_name = track_info['name']
                    artists = ", ".join(artist['name'] for artist in track_info['artists'])
                    print(f" - Track: {track_name}, Artists: {artists}")