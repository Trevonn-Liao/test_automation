# test_automation

Python API automation tests for the Go `feed_system` project.

## Project Structure

```text
test_automation/
├── api/
│   ├── __init__.py
│   └── http_client.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── data/
│   └── test_data.json
├── reports/
│   ├── allure-results/
│   └── allure-report/
├── tests/
│   ├── __init__.py
│   └── test_health.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── run_tests.py
```

## Target Service

The current smoke test covers:

- `GET /health`
- default base URL: `http://localhost:8080`
- expected response:

```json
{
  "code": 0,
  "message": "ok",
  "data": {
    "status": "ok"
  }
}
```

## Quick Start

Start the Go service in one terminal:

```bash
cd /Users/trevonn/TotalFiles/02_code/04_goProject/feed_system
go run ./cmd/server
```

Install Python dependencies:

```bash
cd /Users/trevonn/TotalFiles/02_code/0203_pythonCodes/test_automation
python3 -m pip install -r requirements.txt
```

Run the automation test in another terminal:

```bash
cd /Users/trevonn/TotalFiles/02_code/0203_pythonCodes/test_automation
python3 -m pytest
```

Use a different environment or port when needed:

```bash
API_BASE_URL=http://localhost:8080 python3 -m pytest
```

You can also run the project from an IDE by running:

```bash
python3 run_tests.py
```

## Allure Report

Generate test result files:

```bash
python3 -m pytest --alluredir=reports/allure-results
```

Open the report:

```bash
allure serve reports/allure-results
```

Generate a static HTML report:

```bash
allure generate reports/allure-results -o reports/allure-report --clean
```

Note: `allure-pytest` generates Allure result files. The `allure serve`
command also requires the Allure CLI to be installed on your machine.
