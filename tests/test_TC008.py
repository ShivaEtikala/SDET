from core import assertions
from services.playerName_service import *
import pytest


@pytest.mark.negative
@pytest.mark.regression
def test_TC008_put_playerName_invalid_data(api_client, per_test_logger,get_auth_headers):
    """
    Negative test: Update Player name with invalid data
    """
    logger = per_test_logger
    logger.info("Sending PUT request with invalid data")

    response, payload = put_player_name_invalidpayload(api_client,get_auth_headers)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)
    logger.info("Status Code: %s", response.text)

    # Assertions
    assertions.assert_status_code(response, 400)
    assertions.assert_response_data(response, "Invalid request body format")
    assertions.assert_status_fail(response)
