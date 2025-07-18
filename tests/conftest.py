import pytest
from selene import browser


@pytest.fixture(
    scope="function",
    autouse=True
)
def browser_open_and_quit(browser_options):
    browser.config.driver_options = browser_options
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.quit()