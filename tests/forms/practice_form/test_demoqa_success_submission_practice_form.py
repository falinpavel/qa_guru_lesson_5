from pages.forms.practice_form.page_practice_form import PracticeFormPage


class TestPracticeForm(PracticeFormPage):

    def test_success_submission_practice_form(self):
        self.open_page()
        self.type_first_name(first_name='Ivan')
        self.type_last_name(last_name='Ivanov')
        self.type_user_email(user_email='test@example.com')
        self.choose_gender('Male')
        self.send_keys_user_number(user_number='8800255653')
        self.enable_date_of_birth()
        self.type_subjects('Computer Science')
        self.choose_hobbies('Sports')
        self.upload_file()
        self.type_current_address(address='Moscow')
        self.choose_state_and_city()
        self.submit_form()
        self.should_form_be_submitted(message='Thanks for submitting the form', no_submitted=False)

    def test_successful_filling_table_practice_form(self):
        self.open_page()
        self.type_first_name(first_name='Ivan')
        self.type_last_name(last_name='Ivanov')
        self.type_user_email(user_email='test@example.com')
        self.choose_gender('Male')
        self.send_keys_user_number(user_number='8800255653')
        self.enable_date_of_birth()
        self.type_subjects('Computer Science')
        self.choose_hobbies('Sports')
        self.upload_file()
        self.type_current_address(address='Moscow')
        self.choose_state_and_city()
        self.submit_form()
        self.should_form_be_submitted(message='Thanks for submitting the form', no_submitted=False)
        self.should_table_be_filled(
            full_name='Ivan Ivanov',
            user_email='test@example.com',
            gender='Male',
            user_number='8800255653',
            date_of_birth='23 May,1996',
            subjects='Computer Science',
            hobbies='Sports',
            file='file.txt',
            current_address='Moscow',
            state_and_city='Uttar Pradesh Lucknow'
        )

    def test_submission_form_with_empty_fields(self):
        self.open_page()
        self.submit_form()
        self.should_form_be_submitted(message='Thanks for submitting the form', no_submitted=True)

    # def test_check_texts_on_form(self):
    #     browser.element('.text-center').should(have.text('Practice Form'))
    #     browser.element('.practice-forms-wrapper h5').should(have.text('Student Registration Form'))
    #     browser.element('#userName-wrapper').should(have.exact_text('Name'))
    #     browser.element('#firstName').should(have.attribute('placeholder').value('First Name'))
    #     browser.element('#lastName').should(have.attribute('placeholder').value('Last Name'))
    #     browser.element('#genterWrapper').should(have.text('Gender'))
    #     browser.all('.custom-radio').should(have.size(3)).should(have.exact_texts('Male', 'Female', 'Other'))
    #     browser.element('#userNumber-label').should(have.text('Mobile')).element('small').should(
    #         have.text('(10 Digits)'))
    #     browser.element('#userNumber').should(have.attribute('placeholder').value('Mobile Number'))
    #     browser.element('#dateOfBirth-label').should(have.text('Date of Birth'))
    #     browser.element('#dateOfBirthInput').should(have.attribute('value').value(datetime.now().strftime('%d %b %Y')))
    #     browser.element('#subjectsWrapper').should(have.text('Subjects'))
    #     browser.element('#hobbiesWrapper').should(have.text('Hobbies'))
    #     browser.all('.custom-checkbox').should(have.size(3)).should(have.exact_texts('Sports', 'Reading', 'Music'))
    #     browser.element('#currentAddress-wrapper').should(have.text('Current Address'))
    #     browser.element('#currentAddress').should(have.attribute('placeholder').value('Current Address'))
    #     browser.element('#stateCity-wrapper').should(have.text('State and City'))
