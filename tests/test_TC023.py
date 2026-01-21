from services.roll_service import *
import core.assertions as assertions
import pytest
from core.client import ApiClient


@pytest.mark.negative
@pytest.mark.regression
def test_TC023_rolldie_invalidmethod(api_client, per_test_logger):
    """
    Test Case: API_TC_023  Verify invalid method for endpoint /rolldie/id
    """

    logger = per_test_logger
    logger.info("Starting test: POST /rolldie/1")

    response = delete_roll_die(api_client)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)

    # Assertions
    assertions.assert_status_code(response, 405)



