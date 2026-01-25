from services.playerName_service import *
import core.assertions as assertions
import pytest
from core.client import ApiClient


@pytest.mark.negative
@pytest.mark.regression
def test_TC007_post_playerName(api_client, per_test_logger,player_name,get_auth_headers):
    """
    Test Case: API_TC_007  Verify update playername with Invalid HTTP method POST
    """

    logger = per_test_logger
    logger.info("Starting test: POST /playerName")

    response, payload = post_player_name(api_client,get_auth_headers, player_name)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)

    # Assertions
    assertions.assert_status_code(response, 405)

