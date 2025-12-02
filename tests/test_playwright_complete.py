"""
Complete Playwright E2E tests for JWT authentication
Includes both positive and negative test scenarios
"""
import pytest
from playwright.sync_api import sync_playwright
import time


def test_positive_register_and_login():
    """
    Positive Test: Complete registration and login flow
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            base_url = "http://localhost:8000"
            timestamp = str(int(time.time()))
            username = f"user{timestamp}"
            email = f"user{timestamp}@example.com"
            password = "SecurePass123!"
            
            # Register
            page.goto(f"{base_url}/register")
            page.fill('input[name="username"]', username)
            page.fill('input[name="email"]', email)
            page.fill('input[name="first_name"]', "Test")
            page.fill('input[name="last_name"]', "User")
            page.fill('input[name="password"]', password)
            page.fill('input[name="confirm_password"]', password)
            page.click('button[type="submit"]')
            page.wait_for_url(f"{base_url}/login", timeout=5000)
            
            # Login
            page.fill('input[name="username"]', username)
            page.fill('input[name="password"]', password)
            page.click('button[type="submit"]')
            page.wait_for_url(f"{base_url}/dashboard", timeout=5000)
            
            # Verify tokens
            access_token = page.evaluate("() => localStorage.getItem('access_token')")
            assert access_token is not None, "Access token not stored"
            
            print("✓ Positive test passed: Register and login successful")
            
        finally:
            browser.close()


def test_negative_short_password():
    """
    Negative Test: Registration with password too short
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            base_url = "http://localhost:8000"
            timestamp = str(int(time.time()))
            
            page.goto(f"{base_url}/register")
            page.fill('input[name="username"]', f"short{timestamp}")
            page.fill('input[name="email"]', f"short{timestamp}@example.com")
            page.fill('input[name="first_name"]', "Short")
            page.fill('input[name="last_name"]', "Pass")
            page.fill('input[name="password"]', "Test1")  # Too short
            page.fill('input[name="confirm_password"]', "Test1")
            page.click('button[type="submit"]')
            
            # Wait for error message
            time.sleep(1)
            error_visible = page.locator('#errorAlert').is_visible()
            assert error_visible, "Error alert should be visible"
            
            # Verify still on registration page
            assert page.url == f"{base_url}/register", "Should stay on registration page"
            
            print("✓ Negative test passed: Short password rejected")
            
        finally:
            browser.close()


def test_negative_wrong_password_login():
    """
    Negative Test: Login with incorrect password
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            base_url = "http://localhost:8000"
            timestamp = str(int(time.time()))
            username = f"wrong{timestamp}"
            email = f"wrong{timestamp}@example.com"
            correct_password = "CorrectPass123!"
            
            # First register a user
            page.goto(f"{base_url}/register")
            page.fill('input[name="username"]', username)
            page.fill('input[name="email"]', email)
            page.fill('input[name="first_name"]', "Wrong")
            page.fill('input[name="last_name"]', "Pass")
            page.fill('input[name="password"]', correct_password)
            page.fill('input[name="confirm_password"]', correct_password)
            page.click('button[type="submit"]')
            page.wait_for_url(f"{base_url}/login", timeout=5000)
            
            # Try to login with wrong password
            page.fill('input[name="username"]', username)
            page.fill('input[name="password"]', "WrongPassword123!")
            page.click('button[type="submit"]')
            
            # Wait for error
            time.sleep(1)
            error_visible = page.locator('#errorAlert').is_visible()
            assert error_visible, "Error alert should be visible"
            
            # Verify still on login page
            assert page.url == f"{base_url}/login", "Should stay on login page"
            
            print("✓ Negative test passed: Wrong password rejected")
            
        finally:
            browser.close()


def test_negative_password_mismatch():
    """
    Negative Test: Registration with non-matching passwords
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            base_url = "http://localhost:8000"
            timestamp = str(int(time.time()))
            
            page.goto(f"{base_url}/register")
            page.fill('input[name="username"]', f"mismatch{timestamp}")
            page.fill('input[name="email"]', f"mismatch{timestamp}@example.com")
            page.fill('input[name="first_name"]', "Mismatch")
            page.fill('input[name="last_name"]', "Test")
            page.fill('input[name="password"]', "TestPass123!")
            page.fill('input[name="confirm_password"]', "DifferentPass123!")
            page.click('button[type="submit"]')
            
            # Wait for error
            time.sleep(1)
            error_visible = page.locator('#errorAlert').is_visible()
            assert error_visible, "Error alert should be visible"
            
            # Verify still on registration page
            assert page.url == f"{base_url}/register", "Should stay on registration page"
            
            print("✓ Negative test passed: Password mismatch detected")
            
        finally:
            browser.close()


if __name__ == "__main__":
    print("\n" + "="*60)
    print("Running Playwright E2E Tests")
    print("="*60 + "\n")
    
    test_positive_register_and_login()
    test_negative_short_password()
    test_negative_wrong_password_login()
    test_negative_password_mismatch()
    
    print("\n" + "="*60)
    print("✅ ALL PLAYWRIGHT TESTS PASSED!")
    print("="*60 + "\n")
