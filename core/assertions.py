# assertions.py
# Centralized API response assertions for test automation

VALID_DIE_VALUES_INT = range(1, 7)
VALID_DIE_VALUES_WORD = {"one", "two", "three", "four", "five", "six"}
VALID_DIE_VALUES_DOT = {".", "..", "...", "....", ".....", "......"}


def assert_status_code(response, expected_status):
    """
    Asert that the HTTP response status code matches the expected value.
    """
    actual = response.status_code
    assert actual == expected_status, f"Expected HTTP status{expected_status}, but received {actual}"


def assert_response_not_empty(response):
    """
    Assert that the HTTP response body is not empty.
    """
    assert response.text, "Response body is empty"


def assert_api_status(response, expected_status):
    """
    Assert that the HTTP response status filed indicates success.
    """
    body = response.json()
    actual = body.get("status")
    assert actual == expected_status, f"Expected API status '{expected_status}', but received '{actual}'"


def assert_response_time(response, max_ms):
    """
    Assert that the HTTP response time is within the acceptable threshold.
    """
    elapsed_ms = response.elapsed.total_seconds() * 1000
    assert elapsed_ms <= max_ms, f"Response time {elapsed_ms}ms exceeded limit of {max_ms}ms"


def assert_response_data(response, expected_data):
    """
    Assert that response body contains expected text.
    """
    assert expected_data in response.text, f"Expected '{expected_data}' to be present in response"


# ---------- Dice-specific Assertions ----------
def assert_rolldice_data_response(response):
    """
    Validate response for roll dice endpoint (list of dice).
    """
    body = response.json()
    assert_api_status(response, "success")
    assert "data" in body, "Missing 'data' in response body"
    assert isinstance(body["data"], list)

    for item in body["data"]:
        assert "id" in item, "Missing 'id' in response body"
        assert "value" in item, "Missing 'value' in response body"

        assert item["id"] in range(1, 6), f"Invalid die id : {item['id']}"
        assert item["value"] in VALID_DIE_VALUES_INT, f"Invalid die value : {item['value']}"


def assert_roll_die_response(response):
    """
    Validate response for single die roll.
    """
    body = response.json()
    assert_api_status(response, "success")

    assert "data" in body, "Missing 'data' in response body"
    data = body.get("data")
    assert "id" in data, "Missing 'id' in response body"
    assert "value" in data, "Missing 'value' in response body"
    assert data["value"] in VALID_DIE_VALUES_INT, f"Invalid die value : {data['value']}"


def assert_invalid_die_id_response(response):
    """
    Validate response for invalid die ID.
    """
    body = response.json()
    assert_api_status(response, "failed")
    assert "data" in body, "Missing daa in response body"
    assert body["data"] == "Die ID must be an integer between 1 and 5", (
        "Unexpected Error message for invalid die ID"
    )


# ---------- Value Type Assertions ----------
def assert_die_value_is_int(response):
    """
    Validate die value type as int
    """
    body = response.json()
    value = body["data"]["value"]
    assert isinstance(value, int), f"Expected die value type int, got {type(value)}"


def assert_die_value_is_float_string(response):
    """
    Validate die value type as float
    """
    body = response.json()
    value = body["data"]["value"]
    assert isinstance(value, str), "Die value should be string"
    assert float(value) >= 1, f"Invalid float value: {value}"


def assert_die_value_is_word(response):
    """
    Validate die value type as word
    """
    body = response.json()
    value = body["data"]["value"]
    assert isinstance(value, str), "Die value must be string"
    assert value in VALID_DIE_VALUES_WORD, f"unexpected die value: {value}"


def assert_die_value_is_dot(response):
    """
    Validate die value type as dot
    """
    body = response.json()
    value = body["data"]["value"]
    assert isinstance(value, str), "Die value should be string"
    assert value in VALID_DIE_VALUES_DOT, f"unexpected die value: {value}"


def assert_invalid_accept_header(response):
    """
    Validate Accept Header
    """
    body = response.json()
    assert body.get("data") == "Invalid value in 'Accept' header", "Unexpected error message for invalid Accept header"
