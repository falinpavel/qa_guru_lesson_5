import pytest
from pages.forms.practice_form.page_practice_form import PagePracticeForm


class BaseTest:

    page_practice_form = PagePracticeForm

    @pytest.fixture(autouse=True)
    def setup_method(self, request, driver):
        request.cls.driver = driver
        request.cls.page_practice_form = PagePracticeForm(driver)
