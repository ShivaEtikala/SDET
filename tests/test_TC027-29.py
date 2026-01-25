from services.roll_service import *
import core.assertions as assertions
import pytest


@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.parametrize(
    "die_id,Accept_Header",
    [
        (1,""),
        (2,"application/json"),
        (3,"application/vnd.yahtzee.int+json")
    ]
)
def test_TC027_29_getdieid1(api_client, per_test_logger, die_id, Accept_Header):
    """
    Test Case: API_TC_27-29  get die ID =1 value with given Accept_Header
    """

    logger = per_test_logger
    logger.info("Starting test: GET /die/%s with Accept Header %s", die_id, Accept_Header)

    response = get_die(api_client, die_id,Accept_Header)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)
    logger.info("data for %s is %s", die_id, response.json())
    logger.info("Value of die id is %s", response.json()["data"]["value"])
    # Assertions
    assertions.assert_status_code(response,200)
    assertions.assert_api_status(response,"success")
    assertions.assert_die_value_is_int(response)

