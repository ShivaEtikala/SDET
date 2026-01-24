import pytest

from services.roll_service import *
import core.assertions as assertions


@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.parametrize(
    "die_id , value",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]
)
def test_TC038_setdiediffvalue(api_client, per_test_logger, die_id, value):
    logger = per_test_logger
    logger.info("Starting test : PUT /die with {id:%s,value:%s}", die_id, value)

    response = put_dievalue(api_client, die_id, value)

    logger.info("Status code is %s", response.status_code)

    assertions.assert_status_code(response,204)
