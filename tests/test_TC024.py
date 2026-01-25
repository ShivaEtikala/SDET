from services.roll_service import *
import core.assertions as assertions
import pytest
from core.client import ApiClient


@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.regression
def test_TC024_dice(api_client, per_test_logger):
    """
    Test Case: API_TC_024  Get all DICE values
    """

    logger = per_test_logger
    logger.info("Starting test: get /dice")

    response = get_dice(api_client)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)
    response_json = response.json()
    logger.info(response_json)

    # Assertions
    assertions.assert_status_code(response, 200)
    assertions.assert_rolldice_data_response(response)
