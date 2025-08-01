from base.base_page import BasePage
from const import UPLOADED_FILE


class PagePracticeForm(BasePage):


    FILE = UPLOADED_FILE

    URL = '/automation-practice-form'

    def open_page(self):
        self.browser.open(self.URL)
