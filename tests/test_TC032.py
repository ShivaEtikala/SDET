from services.roll_service import *
import core.assertions as assertions
import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_TC032_getdieid5(api_client, per_test_logger):
    """
    Test Case: API_TC_32  get die ID =5 value with Accept_Header as application/vnd.yahtzee.dots+json
    """

    logger = per_test_logger
    Accept_Header = "application/vnd.yahtzee.dots+json"
    logger.info("Starting test: GET /die/%s with Accept Header %s", 5, Accept_Header)

    response = get_die(api_client, 5,Accept_Header)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)
    logger.info("data for die ID 5 is %s", response.json())
    logger.info("Value of die id is %s", response.json()["data"]["value"])
    # Assertions
    assertions.assert_status_code(response,200)
    assertions.assert_api_status(response, "success")
    assertions.assert_die_value_is_dot(response)

