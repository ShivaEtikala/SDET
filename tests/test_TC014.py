from services.roll_service import *
import core.assertions as assertions
import pytest
from core.client import ApiClient


@pytest.mark.negative
@pytest.mark.regression
def test_TC014_rolldice_invalidmethod(api_client, per_test_logger):
    """
    Test Case: API_TC_014  Verify Roll dice with invalid method GET
    """

    logger = per_test_logger
    logger.info("Starting test: get /rolldice")

    response = get_roll_dice(api_client)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)

    # Assertions
    assertions.assert_status_code(response, 405)



