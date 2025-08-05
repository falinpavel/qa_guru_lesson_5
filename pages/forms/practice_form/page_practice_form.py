from selene import browser, be, have
from const import UPLOADED_FILE


class PracticeFormPage:

    FILE = UPLOADED_FILE

    URL = '/automation-practice-form'

    def open_page(self) -> browser:
        browser.open(self.URL)

    @staticmethod
    def type_first_name(first_name: str) -> None:
        browser.element('#firstName').should(be.blank).type(first_name).should(be.not_.blank).should(
            have.attribute("value").value(first_name))

    @staticmethod
    def type_last_name(last_name: str) -> None:
        browser.element('#lastName').should(be.blank).type(last_name).should(be.not_.blank).should(
            have.attribute("value").value(last_name))

    @staticmethod
    def type_user_email(user_email: str) -> None:
        browser.element('#userEmail').should(be.blank).type(user_email).should(be.not_.blank).should(
            have.attribute("value").value(user_email))

    @staticmethod
    def choose_gender(*genders: str) -> None:
        """
        Method accepts a list of strings
        :param genders:
        :return:
        """
        for gender in genders:
            browser.all('[class="custom-control-label"]').element_by(have.text(gender)).click().should(be.enabled)

    @staticmethod
    def send_keys_user_number(user_number: str) -> None:
        browser.element('#userNumber').should(be.blank).send_keys(user_number).should(be.not_.blank).should(
            have.attribute("value").value(user_number))

    @staticmethod
    def enable_date_of_birth() -> None:
        """
        TODO! Make this method universal, DRY it
        """
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element('option[value="4"]').click()
        browser.element('.react-datepicker__year-select').click().element('option[value="1996"]').click()
        browser.element('div[aria-label="Choose Thursday, May 23rd, 1996"]').click()
        browser.element('#dateOfBirthInput').should(be.not_.blank).should(have.attribute("value").value('23 May 1996'))

    @staticmethod
    def type_subjects(*subjects: str) -> None:
        for subject in subjects:
            browser.element('#subjectsInput').type(subject).should(have.attribute("value").value(subject)).press_enter()

    @staticmethod
    def choose_hobbies(*hobbies: str) -> None:
        for hobby in hobbies:
            browser.all('label[class="custom-control-label"]').element_by(have.text(hobby)).click().should(be.enabled)

    @staticmethod
    def upload_file() -> None:
        browser.element('#uploadPicture').send_keys(UPLOADED_FILE)

    @staticmethod
    def type_current_address(address: str) -> None:
        browser.element('#currentAddress').should(be.blank).type(address).should(be.not_.blank).should(
            have.attribute("value").value(address))

    @staticmethod
    def choose_state_and_city() -> None:
        """
        TODO! Make this method universal, DRY it
        """
        browser.element('#state').click().element('#react-select-3-option-1').click()
        browser.element('#city').click().element('#react-select-4-option-1').click()

    @staticmethod
    def submit_form() -> None:
        browser.element('#submit').click()

    @staticmethod
    def should_form_be_submitted(message: str, no_submitted: bool = False) -> None:
        if no_submitted is False:
            browser.element('#example-modal-sizes-title-lg').should(have.text(message))
        else:
            browser.element('#example-modal-sizes-title-lg').should(be.not_.present)

    @staticmethod
    def should_table_be_filled(full_name: str, user_email: str, gender: str, user_number: str, date_of_birth: str,
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

    @staticmethod
    def should_all_texts_into_form(
            center_text: str,
            form_text_label: str,
            name_text_label: str,
            first_name_placeholder: str,
            last_name_placeholder: str,
            gender_text_label: str,
            gender_text_male: str,
            gender_text_female: str,
            gender_text_other: str,
            number_text_label: str,
            number_text_small: str,
            number_placeholder: str,
            birthday_text_label: str,
            subjects_text_label: str,
            hobbies_text_label: str,
            hobbies_text_sport: str,
            hobbies_text_reed: str,
            hobbies_text_music: str,
            address_text_label: str,
            address_placeholder: str,
            state_city_text_label: str
        ):
        browser.element('.text-center').should(have.text(center_text))
        browser.element('.practice-form-wrapper h5').should(have.text(form_text_label))
        browser.element('#userName-wrapper').should(have.exact_text(name_text_label))
        browser.element('#firstName').should(have.attribute('placeholder').value(first_name_placeholder))
        browser.element('#lastName').should(have.attribute('placeholder').value(last_name_placeholder))
        browser.element('#genterWrapper').should(have.text(gender_text_label))
        browser.all('.custom-radio').should(have.size(3)).should(have.exact_texts(gender_text_male, gender_text_female, gender_text_other))
        browser.element('#userNumber-label').should(have.text(number_text_label)).element('small').should(
            have.text(number_text_small))
        browser.element('#userNumber').should(have.attribute('placeholder').value(number_placeholder))
        browser.element('#dateOfBirth-label').should(have.text(birthday_text_label))
        browser.element('#subjectsWrapper').should(have.text(subjects_text_label))
        browser.element('#hobbiesWrapper').should(have.text(hobbies_text_label))
        browser.all('.custom-checkbox').should(have.size(3)).should(have.exact_texts(hobbies_text_sport, hobbies_text_reed, hobbies_text_music))
        browser.element('#currentAddress-wrapper').should(have.text(address_text_label))
        browser.element('#currentAddress').should(have.attribute('placeholder').value(address_placeholder))
        browser.element('#stateCity-wrapper').should(have.text(state_city_text_label))


