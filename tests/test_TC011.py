import pytest

from services.roll_service import *
import core.assertions as assertions


@pytest.mark.sanity
@pytest.mark.regression
def test_TC011_isyahtzeetrue(api_client, per_test_logger):
    """
    API_TC011 is to check if isyahtzee returns true if all the dice values are same
    :param api_client:
    :param per_test_logger:
    :return:
    """
    logger = per_test_logger
    for die_id in range(1,6):
        logger.info("Starting test : PUT /die with {id:%s,value:1}", die_id)
        response = put_dievalue(api_client, die_id,1)
        logger.info("Status code is %s", response.status_code)
        assertions.assert_status_code(response,204)

    logger.info("Starting test : GET /isYahtzee ")

    response = get_isyahtzee(api_client)
    response_get = get_dice(api_client)

    logger.info("Dice values are %s",response_get.json())

    assertions.assert_status_code(response, 200)
    assertions.assert_status_success(response)
    assertions.assert_response_data(response, "true")

