from core import assertions
from services.playerName_service import *
import pytest


@pytest.mark.negative
@pytest.mark.regression
def test_TC006_put_playerName_wrongusernamepassword(api_client, per_test_logger,player_name):
    """
    Negative test: Update Player name with wrongusernamepassword
    """
    logger = per_test_logger
    logger.info("Sending PUT request with wrong usernamepassword")

    response, payload = put_player_name_wrongusernamepassword(api_client,player_name)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)
    logger.info("Status Code: %s", response.text)

    # Assertions
    assertions.assert_status_code(response, 401)
    assertions.assert_response_data(response, "Incorrect username or password provided")
    assertions.assert_status_fail(response)
