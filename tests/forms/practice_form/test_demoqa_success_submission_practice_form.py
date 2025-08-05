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
        self.type_first_name(first_name='Elena')
        self.type_last_name(last_name='Sidorova')
        self.type_user_email(user_email='Elena123@example.com')
        self.choose_gender('Female')
        self.send_keys_user_number(user_number='8800255612')
        self.enable_date_of_birth()
        self.type_subjects('Maths', 'English')
        self.choose_hobbies('Music')
        self.upload_file()
        self.type_current_address(address='Krasnodar')
        self.choose_state_and_city()
        self.submit_form()
        self.should_form_be_submitted(message='Thanks for submitting the form', no_submitted=False)
        self.should_table_be_filled(
            full_name='Elena Sidorova',
            user_email='Elena123@example.com',
            gender='Female',
            user_number='8800255612',
            date_of_birth='23 May,1996',
            subjects='Maths, English',
            hobbies='Music',
            file='file.txt',
            current_address='Krasnodar',
            state_and_city='Uttar Pradesh Lucknow'
        )

    def test_submission_form_with_empty_fields(self):
        self.open_page()
        self.submit_form()
        self.should_form_be_submitted(message='Thanks for submitting the form', no_submitted=True)

    def test_check_texts_on_form(self):
        self.open_page()
        self.should_all_texts_into_form(
            center_text='Practice Form',
            form_text_label='Student Registration Form',
            name_text_label='Name',
            first_name_placeholder='First Name',
            last_name_placeholder='Last Name',
            gender_text_label='Gender',
            gender_text_male='Male',
            gender_text_female='Female',
            gender_text_other='Other',
            number_text_label='Mobile',
            number_text_small='(10 Digits)',
            number_placeholder='Mobile Number',
            birthday_text_label='Date of Birth',
            subjects_text_label='Subjects',
            hobbies_text_label='Hobbies',
            hobbies_text_sport='Sports',
            hobbies_text_reed='Reading',
            hobbies_text_music='Music',
            address_text_label='Current Address',
            address_placeholder='Current Address',
            state_city_text_label='State and City'
        )
