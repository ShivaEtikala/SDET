from core import assertions
from services.playerName_service import *
import pytest


@pytest.mark.negative
@pytest.mark.regression
def test_TC005_put_playerName_wrongpassword(api_client, per_test_logger,player_name):
    """
    Negative test: Update Player name with wrong password
    """
    logger = per_test_logger
    logger.info("Sending PUT request with wrong password")
    auth_type = AuthType.WRONG_PASSWORD

    response, payload = put_player_name(api_client,player_name,auth_type)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)
    logger.info("Status Code: %s", response.text)

    # Assertions
    assertions.assert_status_code(response, 401)
    assertions.assert_response_data(response, "Incorrect username or password provided")
    assertions.assert_api_status(response, "failed")
