import requests

from utils.logger import get_logger


class ApiClient:
    """
    Centralized HTTP client for RESTAPI interactions.
    All API calls go through this class to ensure:
    -consistent logging
    -centralized request handling
    - Easier debugging and maintenance
    """

    def __init__(self, base_url):
        self.base_url = base_url
        self.logger = get_logger(__name__)

    def get(self, endpoint, headers=None):
        """
        Send HTTP GET request
        :param endpoint: API endpoint path (e.g. /playerName)
        :param headers: Optional HTTP headers
        :return: requests.Response object
        """
        url = f"{self.base_url}{endpoint}"

        # Log request details
        self.logger.info("Sending GET request")
        self.logger.debug("Request URL: %s", url)
        self.logger.debug("Request Headers: %s", headers)

        # Get request with response
        response = requests.get(url, headers=headers)

        # Log response summary
        self.logger.info("Received response")
        self.logger.debug("Response Status Code: %s", response.status_code)
        self.logger.debug("Response Body: %s", response.text)

        return response

    def post(self, endpoint, payload=None, headers=None, auth=None):
        url = f"{self.base_url}{endpoint}"

        # Log request details
        self.logger.info("Sending POST request")
        response = requests.post(url, json=payload, headers=headers, auth=auth)
        # Log response summary
        self.logger.info("Received response")
        return response

    def put(self, endpoint, payload=None, headers=None, auth=None):
        url = f"{self.base_url}{endpoint}"

        # Log request details
        self.logger.info("Sending PUT request")
        response = requests.put(url, json=payload, headers=headers, auth=auth)
        # Log response summary
        self.logger.info("Received response")
        return response

    def delete(self, endpoint, headers=None, auth=None):
        url = f"{self.base_url}{endpoint}"

        # Log request details
        self.logger.info("Sending delete request")
        response = requests.delete(url, headers=headers, auth=auth)
        # Log response summary
        self.logger.info("Received response")
        return response
