def assert_status_code(response, expected):
    """
    Asert that the HTTP response status code matches the expected value.

    This assertion validates that the API returned the correct HTTP status, ensuring the request was processed as
    intended.

    :param response: requests.Response object returned by the API call
    :param expected: Expected HTTP status code (e.g. 200,400, 404_
    :return:
    """
    assert response.status_code == expected, f"Expected {expected}, got {response.status_code}"


def assert_not_empty(response):
    """
    Assert that the HTTP response body is not empty.

    This assertion ensures that the API returned some content in the response, which is especially important for GET
    endpoints returning data.
    """
    assert response.text, "Response body is empty"


def assert_status_success(response):
    """
    Assert that the HTTP response status filed indicates success.

    This assertion validates success by checking the 'status' field in the JSON response body, not just the HTTP
    status code.
    """
    assert response.json().get("status") == "success","Expected response status to be 'success'"


def assert_response_time(response, max_ms):
    """
    Assert that the HTTP response time is within the acceptable threshold.

    This assertion validates basic performance expectations by ensuring the total time taken to receive the response
    code does not exceed the maximum allowed duration.
    """
    assert response.elapsed.total_seconds() * 1000 <= max_ms
