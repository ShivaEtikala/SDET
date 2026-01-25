from services.playerName_service import *
import core.assertions as assertions
import pytest
from core.client import ApiClient


@pytest.mark.regression
def test_TC009_put_playerName_responsetime(api_client, per_test_logger,get_auth_headers,player_name):
    """
    Test Case: API_TC_009  Verify update playername response time
    Verifies:
    -API responds with HTTP statuscode 204
    - After update check the playerName update with get playername service
    Check the response time
    """

    logger = per_test_logger
    logger.info("Starting test: PUT /playerName")

    response, payload = put_player_name(api_client,get_auth_headers,player_name)

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
    logger.info("Response time in ms %s", response.elapsed.total_seconds() * 1000)

    # Assertions
    assertions.assert_status_code(response, 200)
    assertions.assert_not_empty(response)
    assertions.assert_status_success(response)
    assertions.assert_response_time(response, 1000)
    assertions.assert_response_data(response, payload["name"])
