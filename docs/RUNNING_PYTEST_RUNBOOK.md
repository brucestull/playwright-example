# Running Pytest Tests

This guide explains how to run the pytest tests for the Flask Tech Gadget Store application.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   This will install:
   - Flask (web framework)
   - pytest (testing framework)
   - pytest-flask (Flask testing utilities)

## Running Tests

### Run All Tests

To run all pytest tests in the project:

```bash
pytest
```

Or with verbose output:

```bash
pytest -v
```

### Run Tests in a Specific File

To run tests from a specific test file:

```bash
pytest tests/test_app.py
```

### Run a Specific Test

To run a single test function:

```bash
pytest tests/test_app.py::test_index_route -v
```

### Run Tests with Coverage

To see test coverage:

```bash
pip install pytest-cov
pytest --cov=app --cov-report=html
```

This will generate an HTML coverage report in the `htmlcov/` directory.

## Test Structure

The project contains the following pytest tests:

### `tests/test_app.py`

Contains unit tests for the Flask application:

- **`test_index_route`**: Verifies the home page loads successfully
- **`test_index_contains_gadgets`**: Checks that gadgets are displayed on the page
- **`test_api_gadgets_route`**: Tests the API endpoint returns JSON
- **`test_api_gadgets_content`**: Validates the structure of API responses
- **`test_gadget_names_are_funny`**: Ensures gadgets have tech/funny names
- **`test_index_page_structure`**: Verifies HTML structure

## Test Configuration

Tests are configured in `pytest.ini`:

```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
```

## Troubleshooting

### Import Errors

If you encounter import errors, ensure you're running pytest from the project root directory:

```bash
cd /path/to/playwright-example
pytest
```

### Missing Dependencies

If tests fail due to missing dependencies:

```bash
pip install -r requirements.txt
```

### Flask App Not Found

Make sure the `app.py` file and `data/gadgets.json` file exist in the project root.

## Continuous Integration

These tests can be integrated into CI/CD pipelines:

```bash
# Example GitHub Actions
pytest --junitxml=test-results.xml
```

## Next Steps

After running pytest tests, you can also run the Playwright end-to-end tests. See [RUNNING_PLAYWRIGHT_RUNBOOK.md](RUNNING_PLAYWRIGHT_RUNBOOK.md) for details.
