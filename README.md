# Tech Gadget Store - Flask App with Testing

A simple Flask web application showcasing tech gadgets with funny names, complete with comprehensive unit tests (pytest) and end-to-end tests (Playwright).

![Tech Gadget Store](https://github.com/user-attachments/assets/07999358-1729-4913-a013-29c2507f17b6)

## Features

- 🚀 **Flask Web Application**: Displays tech gadgets loaded from JSON data
- 🎭 **Funny Tech Names**: Gadgets like "Quantum Debugger 3000", "AI-Powered Rubber Duck", and "Blockchain Toaster"
- 🧪 **Pytest Unit Tests**: Comprehensive test coverage for Flask routes and functionality
- 🎬 **Playwright E2E Tests**: Browser automation tests for real-world user interactions
- 📚 **Documentation**: Complete runbooks for running both test suites

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-playwright.txt
```

### 2. Install Playwright Browsers

```bash
python -m playwright install chromium
```

### 3. Run the Flask Application

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

**Development Mode:**
To enable Flask debug mode for development (with auto-reload and detailed error pages):

```bash
FLASK_DEBUG=true python app.py
```

**Note:** Debug mode is disabled by default for security. Never enable it in production.

## Testing

### Run Unit Tests (pytest)

```bash
pytest tests/test_app.py -v
```

See [docs/RUNNING_PYTEST_RUNBOOK.md](docs/RUNNING_PYTEST_RUNBOOK.md) for detailed instructions.

### Run E2E Tests (Playwright)

```bash
pytest tests/test_e2e_playwright.py -v
```

See [docs/RUNNING_PLAYWRIGHT_RUNBOOK.md](docs/RUNNING_PLAYWRIGHT_RUNBOOK.md) for detailed instructions.

## Project Structure

```
.
├── app.py                          # Main Flask application
├── data/
│   └── gadgets.json               # Gadget data source
├── templates/
│   └── index.html                 # HTML template
├── tests/
│   ├── conftest.py                # Pytest configuration
│   ├── test_app.py                # Unit tests
│   └── test_e2e_playwright.py     # E2E tests
├── docs/
│   ├── RUNNING_PYTEST_RUNBOOK.md
│   └── RUNNING_PLAYWRIGHT_RUNBOOK.md
├── requirements.txt               # Python dependencies
└── requirements-playwright.txt    # Playwright dependencies
```

## The Gadgets

The store features hilariously named tech gadgets including:

- **Quantum Debugger 3000**: Fixes bugs before you even write them
- **AI-Powered Rubber Duck**: Now with GPT-5! Actually talks back with solutions
- **Blockchain Toaster**: Decentralized bread browning with NFT minting
- **Neural Network Coffee Maker**: Machine learning that makes your morning coffee
- **Serverless Can Opener**: Opens cans without any servers!

## API Endpoints

- `GET /`: Main page displaying all gadgets
- `GET /api/gadgets`: JSON API endpoint for gadget data

## License

This is an example project for demonstrating Flask with testing.