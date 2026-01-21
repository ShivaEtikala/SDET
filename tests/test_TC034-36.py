from services.roll_service import *
import core.assertions as assertions
import pytest
from core.client import ApiClient


@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("die_id",[0,6,'a'])
def test_TC034_36_die_invalidid(api_client, per_test_logger,die_id):
    """
    Test Case: API_TC_34-36  Verify die with invalid id
    """

    logger = per_test_logger
    logger.info("Starting test: GET /die/%s",die_id)

    response = get_die(api_client, die_id)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)
    logger.info("data for %s is %s",die_id, response.json())

    # Assertions
    assertions.assert_status_code(response, 400)
    assertions.assert_rolldie_invaliddata(response)


