# SAS SDET API Automation Project

## Overview

This project contains automated API tests for the SAS SDET API services. The tests are written in **Python** using **pytest** and follow a structured framework for maintainability, logging, and reporting.  

The framework supports:  

- GET, POST, PUT, DELETE API testing  
- Custom logging for requests and responses  
- Assertions for status code, response body, and response time  
- HTML report generation per test run  
- CI/CD integration with **GitHub Actions** or **Jenkins**  

---

## Project Structure
SAS_SDET/
|----core/ #Core utilities
| |---client.py #API client wrapper with logging
| |---assertiona.py #Common assertion methods
|----Services/ #Service functions for API endpoints
| |---get_playerName_service.py
|----tests/ #All testcases
| |---conftest.py #Pytest fixtures
| |---test_TC001_get_playerName.py
|----utils/#Utility modules
| |---logger.py #Custom logger configuration
|----config/ #Environment configuration
| |---dev.yaml
|----reports/ # Test reports generated here
|----requirements.txt #Python dependencies
|----pytest.ini #Pytest configuration


---

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/ShivaEtikala/SDET.git
cd SAS_SDET

2. **Clone the repository:**
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

3. ***Install dependencies***
pip install --upgrade pip
pip install -r requirements.txt

4. ***Configuration***
- API based URL is defined in conftest.py

5. ***Running Tests***
From Terminal
pytest --html=reports/pytest-report.html --self-contained-html -v

6.***Logging***
-Customr logger implemented in utils/logger.py

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
- Aseertions are used for status code, Status successs, response time, Response body not empty

## Requirements
-Python 3.12
-Packages in requirements.txt
pytest
requests
pyyaml
pytest-html

## Notes:
- Ensure Docker is running locally if localhost as API base URL
- For CI/CD, API should run ina  container accessible by the runner
- Use pytest.ini to configure pytest logging and report options

