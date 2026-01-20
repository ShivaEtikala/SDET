import logging
import core.assertions as assertions
from services.get_playerName_service import get_player_name
from utils.logger import get_logger

# Module-Level Logger for this test file
#logger = get_logger(__name__)


def test_tc001_get_playername(api_client, per_test_logger):
    # Below print statements are for debugging logging
    # print("Logger handlers:",logger.handlers)
    # print("Logger propagate:",logger.propagate)

    """
    Test Case: API_TC_001  Verify GET playerName
    Verifies:
    -API responds with HTTP statuscode 200
    -Response body is not empty
    """
    logger = per_test_logger
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
    assertions.assert_not_empty(response)
    assertions.assert_status_success(response)
    assertions.assert_response_time(response, 1000)
