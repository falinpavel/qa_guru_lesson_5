from pages.forms.practice_form.page_practice_form import PracticeFormPage


class TestPracticeForm(PracticeFormPage):

    def test_success_submission_practice_form(self, practice_form_page):
        practice_form_page.open_page()
        practice_form_page.type_first_name(first_name='Ivan')
        practice_form_page.type_last_name(last_name='Ivanov')
        practice_form_page.type_user_email(user_email='test@example.com')
        practice_form_page.choose_gender('Male')
        practice_form_page.send_keys_user_number(user_number='8800255653')
        practice_form_page.enable_date_of_birth()
        practice_form_page.type_subjects('Computer Science')
        practice_form_page.choose_hobbies('Sports')
        practice_form_page.upload_file()
        practice_form_page.type_current_address(address='Moscow')
        practice_form_page.choose_state_and_city()
        practice_form_page.submit_form()
        practice_form_page.should_form_be_submitted(message='Thanks for submitting the form', no_submitted=False)

    def test_successful_filling_table_practice_form(self, practice_form_page):
        practice_form_page.open_page()
        practice_form_page.type_first_name(first_name='Elena')
        practice_form_page.type_last_name(last_name='Sidorova')
        practice_form_page.type_user_email(user_email='Elena123@example.com')
        practice_form_page.choose_gender('Female')
        practice_form_page.send_keys_user_number(user_number='8800255612')
        practice_form_page.enable_date_of_birth()
        practice_form_page.type_subjects('Maths', 'English')
        practice_form_page.choose_hobbies('Music')
        practice_form_page.upload_file()
        practice_form_page.type_current_address(address='Krasnodar')
        practice_form_page.choose_state_and_city()
        practice_form_page.submit_form()
        practice_form_page.should_form_be_submitted(message='Thanks for submitting the form', no_submitted=False)
        practice_form_page.should_table_be_filled(
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

    def test_submission_form_with_empty_fields(self, practice_form_page):
        practice_form_page.open_page()
        practice_form_page.submit_form()
        practice_form_page.should_form_be_submitted(message='Thanks for submitting the form', no_submitted=True)

    def test_check_texts_on_form(self, practice_form_page):
        practice_form_page.open_page()
        practice_form_page.should_all_texts_into_form(
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
