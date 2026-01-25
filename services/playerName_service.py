from requests.auth import HTTPBasicAuth


def get_player_name(api_client, headers=None):
    """
    Retrieve the current player name from the API.

    This service layer method encapsulates the GET /playerName endpoint and acts as a thin wrapper over the API client.
    It keeps testcases clean by separating request construction from test logic.
    :param api_client: Initialized Api client instance used to make HTTP calls.
    :param headers: Optional HTTP headers to include in the request
    :return: requests.Response object containing API response
    """

    return api_client.get(f"/playerName", headers=headers)


def put_player_name(api_client, get_auth_headers, player_name, headers=None):
    """
    update the player name from the API.
    """
    payload = {"name": player_name}
    auth = get_auth_headers
    return api_client.put(f"/playerName", payload, headers=headers, auth=auth), payload


def post_player_name(api_client, get_auth_headers, player_name, headers=None):
    """
    update the player name from the API.
    """
    payload = {"name": player_name}
    auth = get_auth_headers
    return api_client.post(f"/playerName", payload, headers=headers, auth=auth), payload


def put_player_name_noauth(api_client, player_name,headers=None):
    """
    Update the player name with no Authorization
    """
    payload = {"name": player_name}
    return api_client.put(f"/playerName", payload, headers=headers, auth=None), payload


def put_player_name_wrongusername(api_client, player_name, headers=None):
    """
    Update the player name with no Authorization
    """
    payload = {"name": player_name}
    return api_client.put(f"/playerName", payload, headers=headers, auth=HTTPBasicAuth("admin1", "snakeeyes")), payload


def put_player_name_wrongpassword(api_client, player_name, headers=None):
    """
    Update the player name with no Authorization
    """
    payload = {"name": player_name}
    return api_client.put(f"/playerName", payload, headers=headers, auth=HTTPBasicAuth("admin", "snakeeyesz")), payload


def put_player_name_wrongusernamepassword(api_client, player_name, headers=None):
    """
    Update the player name with no Authorization
    """
    payload = {"name": player_name}
    return api_client.put(f"/playerName", payload, headers=headers, auth=HTTPBasicAuth("admin1", "snakeeyesz")), payload


def put_player_name_invalidpayload(api_client, get_auth_headers, headers=None):
    """
    Update the player name with no Authorization
    """
    payload = {"name": 123}
    auth = get_auth_headers
    return api_client.put(f"/playerName", payload, headers=headers, auth=auth), payload
