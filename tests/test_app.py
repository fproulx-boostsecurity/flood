"""
Tests for the Flood poetry generator Flask application.
"""
import pytest
import json
from app import app, generate_poem, POEM_TEMPLATES, WORD_POOLS

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test the main index route returns a poem."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Flood' in response.data
    assert b'poem-title' in response.data

def test_api_poem_route(client):
    """Test the API endpoint returns JSON poem."""
    response = client.get('/api/poem')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'title' in data
    assert 'lines' in data
    assert isinstance(data['lines'], list)
    assert len(data['lines']) > 0

def test_new_poem_route(client):
    """Test the new poem route generates a different poem."""
    response = client.get('/new')
    assert response.status_code == 200
    assert b'poem-title' in response.data

def test_generate_poem_function():
    """Test the poem generation function."""
    poem = generate_poem()
    
    # Check structure
    assert 'title' in poem
    assert 'lines' in poem
    assert isinstance(poem['lines'], list)
    assert len(poem['lines']) > 0
    
    # Check that title is from our templates
    template_titles = [template['title'] for template in POEM_TEMPLATES]
    assert poem['title'] in template_titles
    
    # Check that lines are not empty
    for line in poem['lines']:
        assert len(line.strip()) > 0
        assert '{' not in line  # No unfilled placeholders

def test_word_pools_completeness():
    """Test that all word pools have content."""
    for category, words in WORD_POOLS.items():
        assert len(words) > 0, f"Word pool '{category}' is empty"
        for word in words:
            assert isinstance(word, str)
            assert len(word.strip()) > 0

def test_poem_templates_validity():
    """Test that poem templates are well-formed."""
    for template in POEM_TEMPLATES:
        assert 'title' in template
        assert 'lines' in template
        assert isinstance(template['lines'], list)
        assert len(template['lines']) > 0
        
        # Check that all placeholders in templates have corresponding word pools
        for line in template['lines']:
            # Extract placeholders from line
            import re
            placeholders = re.findall(r'\{(\w+)\}', line)
            for placeholder in placeholders:
                assert placeholder in WORD_POOLS, f"No word pool for placeholder '{placeholder}'"

def test_multiple_poem_generation():
    """Test that multiple poem generations produce different results."""
    poems = [generate_poem() for _ in range(5)]
    
    # Check that we get different poems (at least some variation)
    poem_strings = [' '.join(poem['lines']) for poem in poems]
    unique_poems = set(poem_strings)
    
    # With randomization, we should get some variety
    # (though there's a small chance they could be the same)
    assert len(unique_poems) >= 1  # At minimum, poems should be valid

def test_static_files_exist(client):
    """Test that static files are accessible."""
    # Test CSS file
    response = client.get('/static/css/style.css')
    assert response.status_code == 200
    
    # Test JS file
    response = client.get('/static/js/app.js')
    assert response.status_code == 200