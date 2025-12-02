import pytest
from playwright.sync_api import sync_playwright
import time


def test_full_auth_flow():
    """
    Complete authentication flow test:
    1. Register a user
    2. Login with that user
    3. Verify dashboard access and JWT tokens
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            base_url = "http://localhost:8000"
            timestamp = str(int(time.time()))
            username = f"testuser{timestamp}"
            email = f"test{timestamp}@example.com"
            password = "TestPass123!"
            
            # Test 1: Register
            print("Testing registration...")
            page.goto(f"{base_url}/register")
            page.fill('input[name="username"]', username)
            page.fill('input[name="email"]', email)
            page.fill('input[name="first_name"]', "Test")
            page.fill('input[name="last_name"]', "User")
            page.fill('input[name="password"]', password)
            page.fill('input[name="confirm_password"]', password)
            page.click('button[type="submit"]')
            
            # Wait for redirect to login
            page.wait_for_url(f"{base_url}/login", timeout=5000)
            print("✓ Registration successful")
            
            # Test 2: Login
            print("Testing login...")
            page.fill('input[name="username"]', username)
            page.fill('input[name="password"]', password)
            page.click('button[type="submit"]')
            
            # Wait for redirect to dashboard
            page.wait_for_url(f"{base_url}/dashboard", timeout=5000)
            print("✓ Login successful")
            
            # Test 3: Verify JWT tokens
            print("Checking JWT tokens...")
            access_token = page.evaluate("() => localStorage.getItem('access_token')")
            assert access_token is not None, "Access token not stored"
            print("✓ JWT tokens stored correctly")
            
            print("\n✅ All tests passed!")
            
        finally:
            browser.close()


if __name__ == "__main__":
    test_full_auth_flow()
