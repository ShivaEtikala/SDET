from services.roll_service import *
import core.assertions as assertions
import pytest
from core.client import ApiClient


@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.parametrize("die_id",[1,2,3,4,5])
def test_TC015_19_rolldie(api_client, per_test_logger,die_id):
    """
    Test Case: API_TC_019  Verify Roll dice with id
    """

    logger = per_test_logger
    logger.info("Starting test: POST /rolldie/%s",die_id)

    response = post_roll_die(api_client, die_id)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)
    logger.info("data for %s is %s",die_id, response.json())

    # Assertions
    assertions.assert_status_code(response, 200)
    assertions.assert_rolldie_data(response)


