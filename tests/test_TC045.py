import pytest

from services.roll_service import *
import core.assertions as assertions


@pytest.mark.negative
@pytest.mark.regression
def test_TC045_setdievalue_invalidpassword(api_client, per_test_logger):
    """
    API_TC45 Set Die value with wrong password
    :param api_client:
    :param per_test_logger:
    """
    logger = per_test_logger
    logger.info("Starting test : PUT /die with {id:1,value:1}")

    response = put_dievalue_wrongpassword(api_client, 1, 1)

    logger.info("Status code is %s", response.status_code)
    logger.info("Response is %s", response.json())

    assertions.assert_status_code(response,401)
    assertions.assert_api_status(response,"failed")
    assertions.assert_response_data(response,"Incorrect username or password provided")
