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

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        albums = response.json().get('items', [])
        return albums
    else:
        print("Error retrieving saved albums:", response.json())
        return None

if __name__ == "__main__":
    
    if not check_access_token(ACCESS_TOKEN):
        print("Access token is invalid. Refreshing...")
        ACCESS_TOKEN = get_new_access_token(REFRESH_TOKEN)
    
    saved_albums = get_saved_albums(ACCESS_TOKEN)
    
    if saved_albums:
        print("Saved Albums:")
        for album in saved_albums:
            album_info = album['album']
            print(f"- {album_info['name']} by {', '.join(artist['name'] for artist in album_info['artists'])} (ID: {album_info['id']})")