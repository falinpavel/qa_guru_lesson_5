from selene import browser, be, have
from const import UPLOADED_FILE


class PracticeFormPage:

    FILE = UPLOADED_FILE

    URL = '/automation-practice-form'

    def open_page(self) -> browser:
        browser.open(self.URL)

    def type_first_name(self, first_name: str) -> None:
        browser.element('#firstName').should(be.blank).type(first_name).should(be.not_.blank).should(
            have.attribute("value").value(first_name))

    def type_last_name(self, last_name: str) -> None:
        browser.element('#lastName').should(be.blank).type(last_name).should(be.not_.blank).should(
            have.attribute("value").value(last_name))

    def type_user_email(self, user_email: str) -> None:
        browser.element('#userEmail').should(be.blank).type(user_email).should(be.not_.blank).should(
            have.attribute("value").value(user_email))

    def choose_gender(self, *genders: str) -> None:
        """
        Method accepts a list of strings
        :param genders:
        :return:
        """
        for gender in genders:
            browser.all('[class="custom-control-label"]').element_by(have.text(gender)).click().should(be.enabled)

    def send_keys_user_number(self, user_number: str) -> None:
        browser.element('#userNumber').should(be.blank).send_keys(user_number).should(be.not_.blank).should(
            have.attribute("value").value(user_number))

    def enable_date_of_birth(self) -> None:
        """
        TODO! Make this method universal, DRY it
        """
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element('option[value="4"]').click()
        browser.element('.react-datepicker__year-select').click().element('option[value="1996"]').click()
        browser.element('div[aria-label="Choose Thursday, May 23rd, 1996"]').click()
        browser.element('#dateOfBirthInput').should(be.not_.blank).should(have.attribute("value").value('23 May 1996'))

    def type_subjects(self, *subjects: str) -> None:
        for subject in subjects:
            browser.element('#subjectsInput').type(subject).should(have.attribute("value").value(subject)).press_enter()

    def choose_hobbies(self, *hobbies: str) -> None:
        for hobby in hobbies:
            browser.all('label[class="custom-control-label"]').element_by(have.text(hobby)).click().should(be.enabled)

    def upload_file(self) -> None:
        browser.element('#uploadPicture').send_keys(UPLOADED_FILE)

    def type_current_address(self, address: str) -> None:
        browser.element('#currentAddress').should(be.blank).type(address).should(be.not_.blank).should(
            have.attribute("value").value(address))

    def choose_state_and_city(self) -> None:
        """
        TODO! Make this method universal, DRY it
        """
        browser.element('#state').click().element('#react-select-3-option-1').click()
        browser.element('#city').click().element('#react-select-4-option-1').click()

    def submit_form(self) -> None:
        browser.element('#submit').click()

    def should_form_be_submitted(self, message: str, no_submitted: bool = False) -> None:
        if no_submitted is False:
            browser.element('#example-modal-sizes-title-lg').should(have.text(message))
        else:
            browser.element('#example-modal-sizes-title-lg').should(be.not_.present)

    def should_table_be_filled(self, full_name: str, user_email: str, gender: str, user_number: str, date_of_birth: str,
                               subjects: str, hobbies: str, file: str, current_address: str, state_and_city: str) -> None:
        table_element = browser.all('table.table-dark tbody tr')
        table_element.element_by(have.text('Student Name')).all('td').second.should(have.text(full_name))
        table_element.element_by(have.text('Student Email')).all('td').second.should(have.text(user_email))
        table_element.element_by(have.text('Gender')).all('td').second.should(have.text(gender))
        table_element.element_by(have.text('Mobile')).all('td').second.should(have.text(user_number))
        table_element.element_by(have.text('Date of Birth')).all('td').second.should(have.text(date_of_birth))
        table_element.element_by(have.text('Subjects')).all('td').second.should(have.text(subjects))
        table_element.element_by(have.text('Hobbies')).all('td').second.should(have.text(hobbies))
        table_element.element_by(have.text('Picture')).all('td').second.should(have.text(file))
        table_element.element_by(have.text('Address')).all('td').second.should(have.text(current_address))
        table_element.element_by(have.text('State and City')).all('td').second.should(have.text(state_and_city))
