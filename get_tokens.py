import requests
from urllib.parse import urlencode
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI


SCOPE = (
    "user-library-read "
    "user-library-modify "
    "playlist-read-private "
    "playlist-read-collaborative "
    "playlist-modify-public "
    "playlist-modify-private "
    "user-read-playback-state "
    "user-modify-playback-state "
    "user-read-currently-playing "
    "user-follow-read "
    "user-follow-modify "
    "user-read-recently-played "
    "user-top-read "
    "user-read-private "
    "user-read-email "
    "ugc-image-upload"
)

def get_authorization_url():
    """
    Generate the Spotify authorization URL.
    """
    auth_url = "https://accounts.spotify.com/authorize"
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE,
    }
    return f"{auth_url}?{urlencode(params)}"

def get_tokens(auth_code):
    """
    Exchange the authorization code for access and refresh tokens.
    """
    token_url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    
    response = requests.post(token_url, data=data)

    if response.status_code == 200:
        return response.json()  # Returns both access and refresh tokens
    else:
        print("Error getting tokens:", response.json())
        return None

def refresh_access_token(refresh_token):
    """
    Refresh the access token using the refresh token.
    """
    token_url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    
    response = requests.post(token_url, data=data)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print("Error refreshing access token:", response.json())
        return None

if __name__ == "__main__":
    # Step 1: Get user authorization URL and visit it manually
    print("Go to this URL to authorize your app:")
    print(get_authorization_url())

    # After authorizing, enter the authorization code from the redirect URL
    auth_code = input("Enter the authorization code from the redirected URL: ").strip()

    # Step 2: Get tokens using the authorization code
    tokens = get_tokens(auth_code)

    if tokens:
        access_token = tokens.get("access_token")
        refresh_token = tokens.get("refresh_token")
        
        print(f"Access Token: {access_token}")
        print(f"Refresh Token: {refresh_token}")

        # Example of refreshing access token later
        new_access_token = refresh_access_token(refresh_token)
        
        if new_access_token:
            print(f"New Access Token: {new_access_token}")