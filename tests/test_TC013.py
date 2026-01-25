from services.roll_service import *
import core.assertions as assertions
import pytest
from core.client import ApiClient


@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.regression
def test_TC013_rolldice(api_client, per_test_logger):
    """
    Test Case: API_TC_013  Verify Roll dice
    """

    logger = per_test_logger
    logger.info("Starting test: POST /rolldice")

    response = post_roll_dice(api_client)
    response_json = response.json()

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)
    logger.info(response_json)

    # Assertions
    assertions.assert_status_code(response, 200)
    assertions.assert_rolldice_data_response(response)
