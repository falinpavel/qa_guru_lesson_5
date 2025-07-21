import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="session",autouse=True)
def browser_options():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument('--start-maximized')
    # driver_options.add_argument('--headless')
    browser.config.base_url = 'https://demoqa.com'
    return driver_options
