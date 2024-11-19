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

def update_playlist_details(playlist_id, new_name, new_description, access_token):
    """
    Update the name and description of a specified playlist.
    """
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    data = {
        "name": new_name,
        "description": new_description,
        "public": False  
    }

    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Playlist updated successfully!")
        return True
    else:
        print("Error updating playlist:", response.json())
        return False

if __name__ == "__main__":
    
    if not check_access_token(ACCESS_TOKEN):
        print("Access token is invalid. Refreshing...")
        ACCESS_TOKEN = get_new_access_token(REFRESH_TOKEN)
    
    playlist_name = input("Enter the name of the playlist you want to update: ")
    
    playlist_id = get_playlist_id(playlist_name, ACCESS_TOKEN)
    
    if playlist_id:
        new_name = input("Enter the new name for the playlist: ")
        new_description = input("Enter the new description for the playlist: ")
        
        update_playlist_details(playlist_id, new_name, new_description, ACCESS_TOKEN)