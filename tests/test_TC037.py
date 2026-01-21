from services.roll_service import *
import core.assertions as assertions
import pytest
from core.client import ApiClient


@pytest.mark.negative
@pytest.mark.regression
def test_TC037_die_invalidmethod(api_client, per_test_logger):
    """
    Test Case: API_TC_37  Verify die with invalid method
    """

    logger = per_test_logger
    logger.info("Starting test: DELETE /die/1")

    response = delete_die(api_client)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)

    # Assertions
    assertions.assert_status_code(response, 405)



