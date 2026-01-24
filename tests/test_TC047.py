import pytest

from services.roll_service import *
import core.assertions as assertions


@pytest.mark.negative
@pytest.mark.regression
def test_TC047_setdievalue_invalidmethod(api_client, per_test_logger):
    """
    API_TC47 Set Die value with invalid method
    :param api_client:
    :param per_test_logger:
    """
    logger = per_test_logger
    logger.info("Starting test : DELETE /die with {id:1,value:1}")

    response = delete_dievalue(api_client, 1, 1)

    logger.info("Status code is %s", response.status_code)

    assertions.assert_status_code(response,405)
