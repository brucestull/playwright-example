# Running Playwright End-to-End Tests

This guide explains how to run the Playwright end-to-end (E2E) tests for the Flask Tech Gadget Store application.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Internet connection (for initial browser download)

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-playwright.txt
```

This installs:
- Flask (the web application)
- pytest (testing framework)
- playwright (browser automation)
- pytest-playwright (Playwright pytest plugin)

### 2. Install Playwright Browsers

After installing the Python packages, download the browser binaries:

```bash
python -m playwright install chromium
```

Or install all browsers (Chromium, Firefox, WebKit):

```bash
python -m playwright install
```

## Running Playwright Tests

### Run All E2E Tests

To run all Playwright end-to-end tests:

```bash
pytest tests/test_e2e_playwright.py
```

### Run with Verbose Output

```bash
pytest tests/test_e2e_playwright.py -v
```

### Run a Specific Test

To run a single E2E test:

```bash
pytest tests/test_e2e_playwright.py::test_homepage_loads -v
```

### Run in Headed Mode (with visible browser)

**Note:** Headed mode requires a display server (X11). In most CI environments or headless servers, you must use headless mode (the default).

To run with a visible browser on a machine with a display:

```bash
pytest tests/test_e2e_playwright.py --headed
```

### Run with Different Browsers

Playwright supports multiple browsers. By default, tests run on Chromium.

Run on specific browsers:

```bash
# Firefox only
pytest tests/test_e2e_playwright.py --browser firefox

# WebKit only
pytest tests/test_e2e_playwright.py --browser webkit

# All browsers
pytest tests/test_e2e_playwright.py --browser chromium --browser firefox --browser webkit
```

### Debugging Tests

To debug Playwright tests with the Playwright Inspector:

```bash
PWDEBUG=1 pytest tests/test_e2e_playwright.py
```

### Slow Motion Mode

Run tests in slow motion to see what's happening:

```bash
pytest tests/test_e2e_playwright.py --slowmo 1000
```

The value is in milliseconds (1000 = 1 second delay between actions).

## Test Structure

### `tests/test_e2e_playwright.py`

Contains end-to-end tests that verify the application behavior in a real browser:

- **`test_homepage_loads`**: Verifies the homepage loads with correct title
- **`test_gadgets_are_displayed`**: Checks that gadget cards appear on the page
- **`test_specific_gadgets_exist`**: Validates specific gadgets are visible
- **`test_gadget_card_structure`**: Ensures each card has name, description, and price
- **`test_gadget_prices_displayed`**: Verifies prices are shown with $ symbol
- **`test_hover_effect`**: Tests CSS hover interactions
- **`test_responsive_grid`**: Validates the grid layout

## How the Tests Work

1. **Flask Server**: The tests automatically start the Flask application on `http://localhost:5000`
2. **Browser Automation**: Playwright launches a browser and navigates to the app
3. **Assertions**: Tests verify elements exist, content is correct, and interactions work
4. **Cleanup**: The Flask server and browser are automatically closed after tests

## Troubleshooting

### Browser Not Installed Error

If you see an error about browsers not being installed:

```bash
python -m playwright install chromium
```

### Port Already in Use

If port 5000 is already in use, stop any running Flask processes:

```bash
# On Linux/Mac
pkill -f "python.*app.py"

# Or find and kill the specific process
lsof -i :5000
kill -9 <PID>
```

### Tests Timeout or Fail to Connect

Ensure the Flask app starts correctly:

1. Test manually: `python app.py`
2. Check if port 5000 is accessible: `curl http://localhost:5000`
3. Look for errors in the Flask server logs

### Headless Mode Required

In CI/CD environments without a display:

```bash
# Always run in headless mode (default)
pytest tests/test_e2e_playwright.py

# Or explicitly set headless
pytest tests/test_e2e_playwright.py --browser-headless=true
```

## Taking Screenshots

To capture screenshots during test failures, create a pytest configuration or modify the test:

```python
# In conftest.py or test file
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    if call.when == "call" and call.excinfo is not None:
        page = item.funcargs.get('page')
        if page:
            page.screenshot(path=f"screenshot-{item.name}.png")
```

## Continuous Integration

Example GitHub Actions workflow:

```yaml
- name: Install dependencies
  run: |
    pip install -r requirements.txt
    pip install -r requirements-playwright.txt

- name: Install Playwright browsers
  run: python -m playwright install --with-deps chromium

- name: Run Playwright tests
  run: pytest tests/test_e2e_playwright.py -v
```

## Next Steps

- Review the [pytest runbook](RUNNING_PYTEST_RUNBOOK.md) for unit tests
- Explore [Playwright documentation](https://playwright.dev/python/) for advanced features
- Add more E2E tests as your application grows
