from services.playerName_service import *
import core.assertions as assertions
import pytest
from core.client import ApiClient


@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.regression
def test_TC002_put_playerName(api_client, per_test_logger, player_name, get_auth_headers):
    """
    Test Case: API_TC_002  Verify update playername
    Verifies:
    -API responds with HTTP statuscode 204
    - After update check the playerName update with get playername service
    """

    logger = per_test_logger
    logger.info("Starting test: PUT /playerName")
    auth_type = AuthType.AUTHENTICATION

    response, payload = put_player_name(api_client, player_name, auth_type, get_auth_headers)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)

    # Assertions
    assertions.assert_status_code(response, 204)

    logger.info("Starting test: GET /playerName")

    # Below logging is to check root level logging
    # logging.info("Root Logging check")

    # Execute API call via service Layer
    response = get_player_name(api_client)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)
    logger.info("Response Body: %s", response.text)

    # Assertions
    assertions.assert_status_code(response, 200)
    assertions.assert_response_not_empty(response)
    assertions.assert_api_status(response,"success")
    assertions.assert_response_time(response, 1000)
    assertions.assert_response_data(response, payload["name"])
