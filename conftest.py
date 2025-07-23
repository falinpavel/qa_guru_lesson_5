import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="session",autouse=True)
def browser_options():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument('--window-size=1920,1080')
    browser.config.base_url = 'https://demoqa.com'
    return driver_options


@pytest.fixture(scope="function",autouse=True)
def browser_open_and_quit(browser_options):
    browser.config.driver_options = browser_options
    browser.open('/automation-practice-form')
    yield
    browser.quit()
