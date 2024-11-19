import requests
from config import CLIENT_ID, CLIENT_SECRET

def get_new_access_token(refresh_token):
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

def check_access_token(access_token):
    """
    Check if the access token is valid by making a simple API call.
    """
    url = "https://api.spotify.com/v1/me"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return True  # Token is valid
    elif response.status_code == 401:
        return False  # Token is invalid
    else:
        print("Error checking access token:", response.json())
        return False    