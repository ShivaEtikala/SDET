import sys
import logging
import yaml
import pytest
import pytest_html
from pathlib import Path
import re

# ------------
# Project Root Setup
# ------------
PROJECT_ROOT = Path(__file__).parent.parent.resolve()

# Add project root to sys.path so 'core' and 'services' are always importable
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Reports directory
REPORTS_DIR = PROJECT_ROOT / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

from core.client import ApiClient


@pytest.fixture(scope="session")
def config():
    config_path = PROJECT_ROOT / "config" / "dev.yaml"
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def api_client(config):
    """
    Returns a reusuable API client
    :param config: base_url from config/yaml file
    :return: base_url
    """
    return ApiClient(
        base_url=config["base_url"]
    )


@pytest.fixture
def per_test_logger(request):
    """
    Creates a separate log file per test function
    """
    test_name = request.node.name
    safe_test_name = re.sub(r'[\\/:*?"<>|}]',"_",test_name)
    logs_dir = REPORTS_DIR / "logs"
    logs_dir.mkdir(exist_ok=True)
    logfile = PROJECT_ROOT / "reports" / "logs" / f"{safe_test_name}.log"

    logger = logging.getLogger(test_name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        handler = logging.FileHandler(logfile, mode='w')
        formatter = logging.Formatter("%(asctime)s | %(levelname)s |%(name)s | %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    yield logger

    # Cleanup to avoid duplicate Logs
    handlers = logger.handlers[:]
    for h in handlers:
        h.close()
        logger.removeHandler(h)

    def pytest_configure(config):

        config.option.htmlpath = str(REPORTS_DIR / "pytest-report.html")
        config.option.self_contained_html = True
