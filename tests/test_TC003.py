from core import assertions
from services.playerName_service import *
import pytest


@pytest.mark.negative
@pytest.mark.regression
def test_TC003_put_playerName_noauth(api_client, per_test_logger, player_name):
    """
    Negative test: Update Player name with no Authorization
    """
    logger = per_test_logger
    logger.info("Sending PUT request with no Authorization")
    auth_type = AuthType.NO_AUTHENTICATION

    response, payload = put_player_name(api_client, player_name, auth_type)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)
    logger.info("Status Code: %s", response.text)

    # Assertions
    assertions.assert_status_code(response, 401)
    assertions.assert_response_data(response, "Basic auth missing or could not be parsed")
    assertions.assert_api_status(response, "failed")
