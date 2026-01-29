from requests.auth import HTTPBasicAuth
from enum import Enum


class AuthType(Enum):
    AUTHENTICATION = "with_authentication"
    NO_AUTHENTICATION = "no_authentication"
    WRONG_USERNAME = "wrong_username"
    WRONG_PASSWORD = "wrong_password"
    WRONGBOTH = "wrong_both"


def get_player_name(api_client, headers=None):
    """
    Retrieve the current player name from the API.
    """

    return api_client.get(f"/playerName", headers=headers)


def put_player_name(api_client, player_name, auth_type: AuthType, get_auth_headers=None, headers=None):
    """
    update the player name from the API.
        Valid auth_type values:
        - "with_authentication"      : Use correct credentials from get_auth_headers()
        - "no_authentication"     : No authentication header
        - "wrong_username"  : Invalid username
        - "wrong_password"  : Invalid password
        - "wrong_both"  : Both username and password invalid
    """
    payload = {"name": player_name}
    if auth_type == AuthType.AUTHENTICATION:
        auth = get_auth_headers
    elif auth_type == AuthType.NO_AUTHENTICATION:
        auth = None
    elif auth_type == AuthType.WRONG_USERNAME:
        auth = HTTPBasicAuth("admin1", "snakeeyes")
    elif auth_type == AuthType.WRONG_PASSWORD:
        auth = HTTPBasicAuth("admin", "snakeeyesz")
    elif auth_type == AuthType.WRONGBOTH:
        auth = HTTPBasicAuth("admin1", "snakeeyesz")
    else:
        auth = None

    return api_client.put(f"/playerName", payload, headers=headers, auth=auth), payload


def post_player_name(api_client, get_auth_headers, player_name, headers=None):
    """
    update the player name from the API.
    """
    payload = {"name": player_name}
    auth = get_auth_headers
    return api_client.post(f"/playerName", payload, headers=headers, auth=auth), payload


def put_player_name_invalid_payload(api_client, get_auth_headers, headers=None):
    """
    Update the player name with no Authorization
    """
    payload = {"name": 123}
    auth = get_auth_headers
    return api_client.put(f"/playerName", payload, headers=headers, auth=auth), payload
