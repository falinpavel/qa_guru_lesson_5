import pytest

from pages.forms.practice_form.page_practice_form import PracticeFormPage


@pytest.fixture(scope="function")
def practice_form_page():
    return PracticeFormPage()
