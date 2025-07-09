import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    # Enhanced mobile emulation configuration
    mobileEmulation = {
        'deviceName': 'Pixel 2',
    }

    options = Options()
    options.add_experimental_option("mobileEmulation", mobileEmulation)

    # Additional mobile-friendly options
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # Optional: Add more mobile-specific arguments
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    yield browser
    browser.quit()