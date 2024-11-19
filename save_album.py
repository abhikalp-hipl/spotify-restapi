import requests
from validation import check_access_token, get_new_access_token
from config import ACCESS_TOKEN, REFRESH_TOKEN

def search_album(album_name, access_token):
    """
    Search for an album by name and return its ID.
    """
    url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {access_token}"
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

def save_album(album_id, access_token):
    """
    Save an album for the current user using its ID.
    """
    url = f"https://api.spotify.com/v1/me/albums"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    data = {
        "ids": [album_id] 
    }

    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Album {album_id} saved successfully!")
        return True
    else:
        print("Error saving album:", response.json())
        return False

if __name__ == "__main__":
    
    if not check_access_token(ACCESS_TOKEN):
        print("Access token is invalid. Refreshing...")
        ACCESS_TOKEN = get_new_access_token(REFRESH_TOKEN)
    
    album_name = input("Enter the name of the album you want to save: ")
    
    album_id = search_album(album_name, ACCESS_TOKEN)
    
    if album_id:
        save_album(album_id, ACCESS_TOKEN)