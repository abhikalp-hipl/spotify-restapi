import requests
from validation import check_access_token, get_new_access_token
from config import ACCESS_TOKEN, REFRESH_TOKEN
    
def get_saved_albums(access_token):
    """
    Get a list of saved albums for the current user.
    """
    url = "https://api.spotify.com/v1/me/albums"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    albums = []
    
    while True:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])
            albums.extend(items)
            if data['next']:
                url = data['next'] 
            else:
                break
        else:
            print("Error retrieving saved albums:", response.json())
            return None
    
    return albums

def get_tracks_from_album(album_id, access_token):
    """
    Get all tracks from an album using its ID.
    """
    url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        tracks = response.json().get('items', [])
        return tracks
    else:
        print("Error retrieving tracks:", response.json())
        return None

if __name__ == "__main__":
    
    if not check_access_token(ACCESS_TOKEN):
        print("Access token is invalid. Refreshing...")
        ACCESS_TOKEN = get_new_access_token(REFRESH_TOKEN)
    
    saved_albums = get_saved_albums(ACCESS_TOKEN)
    
    if saved_albums:
        print("Saved Albums and their Tracks:")
        
        for album in saved_albums:
            album_info = album['album']
            album_id = album_info['id']
            album_name = album_info['name']
            
            print(f"\nAlbum: {album_name}")
            
            tracks = get_tracks_from_album(album_id, ACCESS_TOKEN)
            
            if tracks:
                for track in tracks:
                    print(f" - Track: {track['name']} (ID: {track['id']})")