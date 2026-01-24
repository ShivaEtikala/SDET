from services.roll_service import *
import core.assertions as assertions
import pytest


@pytest.mark.negative
@pytest.mark.regression
def test_TC033_getdieid5_invalidheader(api_client, per_test_logger):
    """
    Test Case: API_TC_33  get die ID =5 value with Accept_Header as application/xml
    """

    logger = per_test_logger
    Accept_Header = "application/xml"
    logger.info("Starting test: GET /die/%s with Accept Header %s", 5, Accept_Header)

    response = get_die(api_client, 5,Accept_Header)

    # Log response details for traceability
    logger.info("Status Code: %s", response.status_code)
    logger.info("data for die ID 5 is %s", response.json())
    # Assertions
    assertions.assert_status_code(response,400)
    assertions.assert_status_fail(response)
    assertions.assert_die_invalidheader(response)

