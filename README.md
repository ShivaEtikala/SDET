# SAS SDET API Automation Project

## Overview

This project contains automated API tests for the SAS SDET API services. The tests are written in **Python** using **pytest** and follow a structured framework for maintainability, logging, and reporting.  

The framework supports:  

- GET, POST, PUT, DELETE API testing  
- Custom logging for requests and responses  
- Assertions for status code, response body, and response time  
- HTML report generation per test run  
- CI/CD integration with **GitHub Actions** or **Jenkins**  


```

## Project Structure
SAS_SDET/
├── core/                      # Core framework components
│   ├── client.py              # API client wrapper (HTTP calls, logging, retries)
│   └── assertions.py          # Common assertion/helper methods
│
├── services/                  # Service-layer functions for API endpoints
│   └── get_playerName_service.py
│
├── tests/                     # All pytest test cases
│   ├── conftest.py             # Pytest fixtures (config, API client, auth)
│   └── test_TC001_get_playerName.py
│
├── utils/                     # Shared utility modules
│   └── logger.py              # Custom logger configuration
│
├── config/                    # Environment-specific configuration
│   └── dev.yaml               # Base config (overridden by env variables)
│
├── reports/                   # Generated test reports (ignored in Git)
│
├── requirements.txt           # Python dependencies
├── pytest.ini                 # Pytest configuration
├── Dockerfile                 # Docker image definition for test execution
├── .dockerignore              # Files excluded from Docker build context
├── .gitignore                 # Files excluded from Git
└── README.md                  # Project documentation

```

## Setup

```bash
1. **Clone the repository
git clone https://github.com/ShivaEtikala/SDET.git
cd SAS_SDET

2. **Create virtual environment**
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

3. ***Install dependencies***
pip install --upgrade pip
pip install -r requirements.txt

4. ***Configuration***
- API based URL is defined in dev.yaml file

5. ***Running Tests***
From Terminal
pytest --html=reports/pytest-report.html --self-contained-html -v

6.***Logging***
-Custom logger implemented in utils/logger.py

7. ***HTML Reports***
- Configured to generate reports in reports/pytest-report.html

## CI/CD Integration

GitHub Actions:
- Workflow file: .github/workflows/api-test.yml
- Steps:
      1. Checkout code
      2. Setup Python 3.12
      3. Install dependencies
      4. Start API Docker container
      5. Wait for APi readiness
      6. Run test with HTML report
      7. Upload report as artifact

## Test Guidelines
- All tests should start with test_ for pytest to discover them
- Each test logs request and response details
- Assertions are used for status code, Status successs, response time, Response body not empty

## Requirements
-Python 3.12
-Packages in requirements.txt
pytest
requests
pyyaml
pytest-html

## Notes:
- Ensure Docker is running locally if localhost as API in a base URL
- For CI/CD, API should run ina  container accessible by the runner
- Use pytest.ini to configure pytest logging and report options

