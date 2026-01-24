import pytest

from services.roll_service import delete_isyahtzee
import core.assertions as assertions

@pytest.mark.negative
@pytest.mark.regression
def test_TC012_invalidisYahtzee(api_client,per_test_logger):
    """
    API_TC011 is to check if isyahtzee takes invalid HTTP method
    :param api_client:
    :param per_test_logger:
    :return:
    """
    logger=per_test_logger
    logger.info("Send DELETE to /isYahtzee endpoint")

    response = delete_isyahtzee(api_client)

    assertions.assert_status_code(response,405)