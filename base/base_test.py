import pytest
from pages.forms.practice_form.page_practice_form import PagePracticeForm


class BaseTest:

    page_practice_form = PagePracticeForm

    @pytest.fixture(autouse=True)
    def setup_method(self, request, browser_open_and_quit):
        request.cls.browser_settings = browser_open_and_quit
        request.cls.page_practice_form = PagePracticeForm(browser_open_and_quit)
