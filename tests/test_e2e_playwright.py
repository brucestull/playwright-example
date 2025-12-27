"""
Playwright end-to-end tests for the Flask gadget store app.
"""
import pytest
import subprocess
import time
import signal
import os
import sys
import urllib.request
import urllib.error
from playwright.sync_api import Page, expect


def wait_for_server(url, timeout=10, interval=0.5):
    """Wait for server to be ready by polling the endpoint."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            urllib.request.urlopen(url, timeout=1)
            return True
        except (urllib.error.URLError, ConnectionError):
            time.sleep(interval)
    return False


@pytest.fixture(scope="module")
def flask_server():
    """Start Flask server for testing."""
    # Start Flask server in a subprocess
    env = os.environ.copy()
    env["FLASK_APP"] = "app.py"
    
    # Use cross-platform process management
    if sys.platform == 'win32':
        # Windows doesn't support preexec_fn
        process = subprocess.Popen(
            ["python", "app.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env
        )
    else:
        # Unix/Linux/Mac
        process = subprocess.Popen(
            ["python3", "app.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
            preexec_fn=os.setsid
        )
    
    # Wait for server to be ready with retry mechanism
    server_url = "http://localhost:5000"
    if not wait_for_server(server_url, timeout=10):
        # Cleanup on failure
        if sys.platform == 'win32':
            process.terminate()
        else:
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        process.wait()
        pytest.fail("Flask server failed to start within timeout period")
    
    yield server_url
    
    # Cleanup: kill the process
    if sys.platform == 'win32':
        process.terminate()
    else:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    process.wait()


def test_homepage_loads(page: Page, flask_server):
    """Test that the homepage loads successfully."""
    page.goto(flask_server)
    
    # Check page title
    expect(page).to_have_title("Tech Gadget Store")
    
    # Check main heading
    heading = page.locator("h1")
    expect(heading).to_have_text("🚀 Tech Gadget Store")


def test_gadgets_are_displayed(page: Page, flask_server):
    """Test that gadgets are displayed on the page."""
    page.goto(flask_server)
    
    # Check that gadget cards exist
    gadget_cards = page.locator(".gadget-card")
    expect(gadget_cards).not_to_have_count(0)
    
    # Verify we have at least 5 gadgets
    count = gadget_cards.count()
    assert count >= 5, f"Expected at least 5 gadgets, but found {count}"


def test_specific_gadgets_exist(page: Page, flask_server):
    """Test that specific gadgets are present on the page."""
    page.goto(flask_server)
    
    # Check for specific gadget names
    expect(page.locator("text=Quantum Debugger 3000")).to_be_visible()
    expect(page.locator("text=AI-Powered Rubber Duck")).to_be_visible()
    expect(page.locator("text=Blockchain Toaster")).to_be_visible()


def test_gadget_card_structure(page: Page, flask_server):
    """Test that gadget cards have proper structure."""
    page.goto(flask_server)
    
    # Get first gadget card
    first_card = page.locator(".gadget-card").first
    
    # Check card has name
    name = first_card.locator(".gadget-name")
    expect(name).to_be_visible()
    
    # Check card has description
    description = first_card.locator(".gadget-description")
    expect(description).to_be_visible()
    
    # Check card has price
    price = first_card.locator(".gadget-price")
    expect(price).to_be_visible()


def test_gadget_prices_displayed(page: Page, flask_server):
    """Test that gadget prices are visible."""
    page.goto(flask_server)
    
    # Check that prices are displayed with $ symbol
    prices = page.locator(".gadget-price")
    first_price = prices.first
    expect(first_price).to_contain_text("$")


def test_hover_effect(page: Page, flask_server):
    """Test that gadget cards respond to hover."""
    page.goto(flask_server)
    
    # Get first gadget card
    first_card = page.locator(".gadget-card").first
    
    # Hover over the card (this tests the CSS hover state is set up)
    first_card.hover()
    
    # Card should still be visible after hover
    expect(first_card).to_be_visible()


def test_responsive_grid(page: Page, flask_server):
    """Test that the gadget grid is present."""
    page.goto(flask_server)
    
    # Check that the grid container exists
    grid = page.locator(".gadget-grid")
    expect(grid).to_be_visible()
    
    # Grid should contain multiple cards
    cards_in_grid = grid.locator(".gadget-card")
    expect(cards_in_grid).not_to_have_count(0)
