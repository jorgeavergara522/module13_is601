import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def fastapi_server():
    """
    Returns the base URL of the FastAPI server.
    Assumes docker-compose is already running.
    """
    return "http://localhost:8000"


@pytest.fixture(scope="function")
def page(fastapi_server):
    """
    Provides a fresh Playwright page for each test.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        yield page
        
        page.close()
        context.close()
        browser.close()
