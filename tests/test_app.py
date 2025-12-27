"""
Unit tests for Flask app routes and functionality.
"""
import json


def test_index_route(client):
    """Test that the index route loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Tech Gadget Store' in response.data


def test_index_contains_gadgets(client):
    """Test that gadgets are displayed on the index page."""
    response = client.get('/')
    assert response.status_code == 200
    # Check for specific gadget names
    assert b'Quantum Debugger 3000' in response.data
    assert b'AI-Powered Rubber Duck' in response.data
    assert b'Blockchain Toaster' in response.data


def test_api_gadgets_route(client):
    """Test that the API endpoint returns JSON data."""
    response = client.get('/api/gadgets')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    
    data = json.loads(response.data)
    assert 'gadgets' in data
    assert isinstance(data['gadgets'], list)


def test_api_gadgets_content(client):
    """Test that the API returns the expected gadgets."""
    response = client.get('/api/gadgets')
    data = json.loads(response.data)
    
    gadgets = data['gadgets']
    assert len(gadgets) > 0
    
    # Check first gadget structure
    first_gadget = gadgets[0]
    assert 'id' in first_gadget
    assert 'name' in first_gadget
    assert 'description' in first_gadget
    assert 'price' in first_gadget


def test_gadget_names_are_funny(client):
    """Test that gadget names contain tech/funny elements."""
    response = client.get('/api/gadgets')
    data = json.loads(response.data)
    
    gadgets = data['gadgets']
    # Just verify we have some gadgets with fun names
    gadget_names = [g['name'] for g in gadgets]
    
    # Check that we have some gadgets
    assert len(gadget_names) > 0
    
    # Verify at least one gadget has numbers or tech terms
    has_tech_terms = any(
        any(term in name.lower() for term in ['quantum', 'ai', 'blockchain', 'neural', 'serverless'])
        for name in gadget_names
    )
    assert has_tech_terms


def test_index_page_structure(client):
    """Test that the HTML page has the expected structure."""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    # Check for essential HTML elements
    assert '<html' in html
    assert '</html>' in html
    assert 'gadget-card' in html
    assert 'gadget-name' in html
    assert 'gadget-price' in html
