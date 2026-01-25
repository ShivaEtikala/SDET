import pytest

from services.roll_service import *
import core.assertions as assertions


@pytest.mark.negative
@pytest.mark.regression
def test_TC043_setdievalue_noauth(api_client, per_test_logger):
    """
    API_TC41_42 Checking invalid die ID value data
    :param api_client:
    :param per_test_logger:
    """
    logger = per_test_logger
    logger.info("Starting test : PUT /die with {id:1,value:1}")

    response = put_dievalue_withoutautinput(api_client, 1, 1)

    logger.info("Status code is %s", response.status_code)
    logger.info("Response is %s", response.json())

    assertions.assert_status_code(response,401)
    assertions.assert_api_status(response,"failed")
    assertions.assert_response_data(response,"Basic auth missing or could not be parsed")
