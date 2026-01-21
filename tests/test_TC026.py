from services.roll_service import *
import core.assertions as assertions
import pytest
from core.client import ApiClient


@pytest.mark.negative
@pytest.mark.regression
def test_TC026_dicewithids(api_client, per_test_logger):
    """
    Test Case: API_TC_026  Get all DICE values with ids, invalid path
    """

    logger = per_test_logger
    logger.info("Starting test: get /dice/1")

    response = get_dice_withid(api_client)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)

    # Assertions
    assertions.assert_status_code(response, 404)



