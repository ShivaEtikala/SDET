import requests

from utils.logger import get_logger
from urllib.parse import urljoin


class ApiClient:
    """
    Centralized HTTP client for RESTAPI interactions.
    All API calls go through this class to ensure:
    -consistent logging
    -centralized request handling
    - Easier debugging and maintenance
    """

    def __init__(self, base_url, timeout=10):
        self.base_url = base_url
        self.timeout = timeout
        self.logger = get_logger(__name__)

    def _request(self, method, endpoint, payload=None, headers=None, auth=None):
        url = urljoin(self.base_url, endpoint)

        # Log request details
        self.logger.info("Sending %s request to %s", method.upper(), endpoint)
        self.logger.debug("Request URL: %s", url)
        self.logger.debug("Request Headers: %s", headers)
        self.logger.debug("Request Payload: %s", payload)

        # Request with response
        response = requests.request(method=method, url=url, json=payload, headers=headers, auth=auth,
                                    timeout=self.timeout)

        # Log response summary
        self.logger.info("Received response from %s", endpoint)
        self.logger.debug("Response Status Code: %s", response.status_code)
        self.logger.debug("Response Body: %s", response.text)

        return response

    def get(self, endpoint, headers=None, auth=None):
        """
        Send HTTP GET request
        :param endpoint: API endpoint path (e.g. /playerName)
        :param headers: Optional HTTP headers
        :return: requests.Response object
        """
        get_response = self._request("get", endpoint, headers=headers, auth=auth)
        return get_response

    def post(self, endpoint, payload=None, headers=None, auth=None):
        """
        Send HTTP POST request
        :param endpoint: API endpoint path (e.g. /playerName)
        :param payload: Input data
        :param headers: Optional HTTP headers
        :return: requests.Response object
        """
        post_response = self._request("post", endpoint, payload, headers, auth)
        return post_response

    def put(self, endpoint, payload=None, headers=None, auth=None):
        """
        Send HTTP PUT request
        :param endpoint: API endpoint path (e.g. /playerName)
        :param payload: Input data
        :param headers: Optional HTTP headers
        :return: requests.Response object
        """
        put_response = self._request("put", endpoint, payload, headers, auth)
        return put_response

    def delete(self, endpoint, headers=None, auth=None):
        """
        Send HTTP DELETE request
        :param endpoint: API endpoint path (e.g. /playerName)
        :param headers: Optional HTTP headers
        :return: requests.Response object
        """
        delete_response = self._request("delete", endpoint, headers=headers, auth=auth)
        return delete_response
