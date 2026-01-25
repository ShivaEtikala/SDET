from services.roll_service import *
import core.assertions as assertions
import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_TC030_getdieid4(api_client, per_test_logger):
    """
    Test Case: API_TC_30  get die ID =4 value with Accept_Header as application/vnd.yahtzee.float+json
    """

    logger = per_test_logger
    Accept_Header = "application/vnd.yahtzee.float+json"
    logger.info("Starting test: GET /die/%s with Accept Header %s", 4, Accept_Header)

    response = get_die(api_client, 4,Accept_Header)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)
    logger.info("data for die ID 4 is %s", response.json())
    logger.info("Value of die id is %s", response.json()["data"]["value"])
    # Assertions
    assertions.assert_status_code(response,200)
    assertions.assert_api_status(response,"success")
    assertions.assert_die_value_is_float_string(response)

