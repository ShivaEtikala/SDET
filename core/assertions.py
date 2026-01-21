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
    assert response.json().get("status") == "success", "Expected response status to be 'success'"


def assert_response_time(response, max_ms):
    """
    Assert that the HTTP response time is within the acceptable threshold.

    This assertion validates basic performance expectations by ensuring the total time taken to receive the response
    code does not exceed the maximum allowed duration.
    """
    assert response.elapsed.total_seconds() * 1000 <= max_ms


def assert_response_data(response, expecteddata):
    assert expecteddata in response.text


def assert_status_fail(response):
    """
    Assert that the HTTP response status filed indicates failed.
    This assertion validates success by checking the 'status' field in the JSON response body, not just the HTTP
    status code.
    """
    assert response.json().get("status") == "failed", "Expected response status to be 'failed'"


def assert_rolldice_data(response):
    response_json = response.json()
    assert response.json().get("status") == "success", "Expected response status to be 'success'"
    assert "data" in response_json
    assert isinstance(response_json["data"], list)

    for item in response_json["data"]:
        assert "id" in item
        assert "value" in item

        assert 1 <= item["id"] <= 5, f"Invalid id : {item['id']}"
        assert 1 <= item["value"] <= 6, f"Invalid value : {item['value']}"


def assert_rolldie_data(response):
    response_json = response.json()
    assert response.json().get("status") == "success", "Expected response status to be 'success'"
    assert "data" in response_json
    assert "id" in response_json["data"]
    assert "value" in response_json["data"]
    # assert 1 <= response_json["data"]["id"] <= 5, f"Invalid id : {item['id']}"
    assert 1 <= response_json["data"]["value"] <= 6, f"Invalid value : {response_json["data"]["value"]}"


def assert_rolldie_invaliddata(response):
    response_json = response.json()
    assert response.json().get("status") == "failed", "Expected response status to be 'failed'"
    assert "data" in response_json
    assert response_json["data"] == "Die ID must be an integer between 1 and 5"


