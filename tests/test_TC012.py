from services.roll_service import delete_isyahtzee
import core.assertions as assertions

def test_TC012_invalidisYahtzee(api_client,per_test_logger):
    logger=per_test_logger
    logger.info("Send DELETE to /isYahtzee endpoint")

    response = delete_isyahtzee(api_client)

    assertions.assert_status_code(response,405)