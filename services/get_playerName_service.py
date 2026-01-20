from core.client import ApiClient


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
