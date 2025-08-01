import pytest
from selenium import webdriver


@pytest.fixture(scope="function",autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument('--window-size=1920,1080')
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()
