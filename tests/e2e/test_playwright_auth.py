import pytest
from playwright.sync_api import Page, expect
import time

@pytest.mark.e2e
def test_register_with_valid_data(page: Page, fastapi_server: str):
    """Positive Test: Register with valid data"""
    page.goto(f"{fastapi_server}/register")
    
    timestamp = str(int(time.time()))
    username = f"testuser{timestamp}"
    email = f"test{timestamp}@example.com"
    
    page.fill('input[name="username"]', username)
    page.fill('input[name="email"]', email)
    page.fill('input[name="first_name"]', "Test")
    page.fill('input[name="last_name"]', "User")
    page.fill('input[name="password"]', "TestPass123!")
    page.fill('input[name="confirm_password"]', "TestPass123!")
    
    page.click('button[type="submit"]')
    
    success_alert = page.locator('#successAlert')
    expect(success_alert).to_be_visible(timeout=5000)
    expect(success_alert).to_contain_text("Registration successful")
    
    page.wait_for_url(f"{fastapi_server}/login", timeout=5000)
    expect(page).to_have_url(f"{fastapi_server}/login")


@pytest.mark.e2e
def test_login_with_correct_credentials(page: Page, fastapi_server: str):
    """Positive Test: Login with correct credentials"""
    timestamp = str(int(time.time()))
    username = f"loginuser{timestamp}"
    email = f"login{timestamp}@example.com"
    password = "SecurePass123!"
    
    page.goto(f"{fastapi_server}/register")
    page.fill('input[name="username"]', username)
    page.fill('input[name="email"]', email)
    page.fill('input[name="first_name"]', "Login")
    page.fill('input[name="last_name"]', "Test")
    page.fill('input[name="password"]', password)
    page.fill('input[name="confirm_password"]', password)
    page.click('button[type="submit"]')
    
    page.wait_for_url(f"{fastapi_server}/login", timeout=5000)
    
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', password)
    page.click('button[type="submit"]')
    
    success_alert = page.locator('#successAlert')
    expect(success_alert).to_be_visible(timeout=5000)
    
    page.wait_for_url(f"{fastapi_server}/dashboard", timeout=5000)
    expect(page).to_have_url(f"{fastapi_server}/dashboard")
    
    access_token = page.evaluate("() => localStorage.getItem('access_token')")
    assert access_token is not None, "Access token not stored"


@pytest.mark.e2e
def test_register_with_short_password(page: Page, fastapi_server: str):
    """Negative Test: Register with short password"""
    page.goto(f"{fastapi_server}/register")
    
    timestamp = str(int(time.time()))
    
    page.fill('input[name="username"]', f"shortpass{timestamp}")
    page.fill('input[name="email"]', f"short{timestamp}@example.com")
    page.fill('input[name="first_name"]', "Short")
    page.fill('input[name="last_name"]', "Pass")
    page.fill('input[name="password"]', "Test1")
    page.fill('input[name="confirm_password"]', "Test1")
    
    page.click('button[type="submit"]')
    
    error_alert = page.locator('#errorAlert')
    expect(error_alert).to_be_visible(timeout=5000)
    expect(error_alert).to_contain_text("Password must be at least 8 characters")
    
    expect(page).to_have_url(f"{fastapi_server}/register")


@pytest.mark.e2e
def test_login_with_wrong_password(page: Page, fastapi_server: str):
    """Negative Test: Login with wrong password"""
    timestamp = str(int(time.time()))
    username = f"wrongpass{timestamp}"
    email = f"wrong{timestamp}@example.com"
    correct_password = "CorrectPass123!"
    
    page.goto(f"{fastapi_server}/register")
    page.fill('input[name="username"]', username)
    page.fill('input[name="email"]', email)
    page.fill('input[name="first_name"]', "Wrong")
    page.fill('input[name="last_name"]', "Pass")
    page.fill('input[name="password"]', correct_password)
    page.fill('input[name="confirm_password"]', correct_password)
    page.click('button[type="submit"]')
    
    page.wait_for_url(f"{fastapi_server}/login", timeout=5000)
    
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', "WrongPassword123!")
    page.click('button[type="submit"]')
    
    error_alert = page.locator('#errorAlert')
    expect(error_alert).to_be_visible(timeout=5000)
    
    expect(page).to_have_url(f"{fastapi_server}/login")


@pytest.mark.e2e
def test_register_with_mismatched_passwords(page: Page, fastapi_server: str):
    """Negative Test: Passwords don't match"""
    page.goto(f"{fastapi_server}/register")
    
    timestamp = str(int(time.time()))
    
    page.fill('input[name="username"]', f"mismatch{timestamp}")
    page.fill('input[name="email"]', f"mismatch{timestamp}@example.com")
    page.fill('input[name="first_name"]', "Mismatch")
    page.fill('input[name="last_name"]', "Test")
    page.fill('input[name="password"]', "TestPass123!")
    page.fill('input[name="confirm_password"]', "DifferentPass123!")
    
    page.click('button[type="submit"]')
    
    error_alert = page.locator('#errorAlert')
    expect(error_alert).to_be_visible(timeout=5000)
    expect(error_alert).to_contain_text("Passwords do not match")
    
    expect(page).to_have_url(f"{fastapi_server}/register")
