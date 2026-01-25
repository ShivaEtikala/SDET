import pytest

from services.roll_service import *
import core.assertions as assertions


@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize(
    "die_id , value",
    [
        (1, 8),
        (2, 0),
    ]
)
def test_TC041_42_setdiediffvalue(api_client, per_test_logger, get_auth_headers, die_id, value):
    """
    API_TC41_42 Checking invalid die ID value data
    :param api_client:
    :param per_test_logger:
    :param die_id:
    :param value:
    :return:
    """
    logger = per_test_logger
    logger.info("Starting test : PUT /die with {id:%s,value:%s}", die_id, value)

    response = put_dievalue(api_client, die_id, value,get_auth_headers)

    logger.info("Status code is %s", response.status_code)
    logger.info("Response is %s", response.json())

    assertions.assert_status_code(response,400)
    assertions.assert_status_fail(response)
    assertions.assert_response_data(response,"Die value must be between 1 and 6")
