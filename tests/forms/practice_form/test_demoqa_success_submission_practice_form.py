import os
from selene import browser, have, be
from datetime import datetime
from selene.support.shared.jquery_style import s, ss

UPLOADED_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file.txt")


def test_success_submission_students_registration_form():
    s('#firstName').should(be.blank).type('Ivan').should(be.not_.blank).should(have.attribute("value").value('Ivan'))
    s('#lastName').should(be.blank).type('Ivanov').should(be.not_.blank).should(have.attribute("value").value('Ivanov'))
    s('#userEmail').should(be.blank).type('test@example.com').should(be.not_.blank).should(have.attribute("value").value('test@example.com'))
    s('label[for="gender-radio-1"]').click().should(be.enabled)
    s('#userNumber').should(be.blank).send_keys('8800255653').should(be.not_.blank).should(have.attribute("value").value('8800255653'))
    s('#dateOfBirthInput').click()
    s('.react-datepicker__month-select').click().s('option[value="4"]').click()
    s('.react-datepicker__year-select').click().s('option[value="1996"]').click()
    s('div[aria-label="Choose Thursday, May 23rd, 1996"]').click()
    s('#dateOfBirthInput').should(be.not_.blank).should(have.attribute("value").value('23 May 1996'))
    s('#subjectsInput').type('Computer Science').should(have.attribute("value").value('Computer Science')).press_enter()
    ss('label[class="custom-control-label"]').element_by(have.text('Sports')).click().should(be.enabled)
    s('#uploadPicture').send_keys(os.path.abspath(UPLOADED_FILE))
    s('#currentAddress').should(be.blank).type('Moscow').should(be.not_.blank).should(have.attribute("value").value('Moscow'))
    s('#state').click().s('#react-select-3-option-1').click()
    s('#city').click().s('#react-select-4-option-1').click()
    s('#submit').click()
    s('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))


def test_successful_filling_table():
    test_success_submission_students_registration_form()
    table_element = ss('table.table-dark tbody tr')
    table_element.element_by(have.text('Student Name')).ss('td').second.should(have.text('Ivan Ivanov'))
    table_element.element_by(have.text('Student Email')).ss('td').second.should(have.text('test@example.com'))
    table_element.element_by(have.text('Gender')).ss('td').second.should(have.text('Male'))
    table_element.element_by(have.text('Mobile')).ss('td').second.should(have.text('8800255653'))
    table_element.element_by(have.text('Date of Birth')).all('td').second.should(have.text('23 May,1996'))
    table_element.element_by(have.text('Subjects')).ss('td').second.should(have.text('Computer Science'))
    table_element.element_by(have.text('Hobbies')).ss('td').second.should(have.text('Sports'))
    table_element.element_by(have.text('Picture')).ss('td').second.should(have.text('file.txt'))
    table_element.element_by(have.text('Address')).ss('td').second.should(have.text('Moscow'))
    table_element.element_by(have.text('State and City')).ss('td').second.should(have.text('Uttar Pradesh Lucknow'))


def test_submission_form_with_empty_fields():
    s('#submit').click()
    s('#example-modal-sizes-title-lg').should(be.absent)


def test_check_texts_on_form():
    s('.text-center').should(have.text('Practice Form'))
    s('.practice-form-wrapper h5').should(have.text('Student Registration Form'))
    s('#userName-wrapper').should(have.exact_text('Name'))
    s('#firstName').should(have.attribute('placeholder').value('First Name'))
    s('#lastName').should(have.attribute('placeholder').value('Last Name'))
    s('#genterWrapper').should(have.text('Gender'))
    ss('.custom-radio').should(have.size(3)).should(have.exact_texts('Male', 'Female', 'Other'))
    s('#userNumber-label').should(have.text('Mobile')).s('small').should(have.text('(10 Digits)'))
    s('#userNumber').should(have.attribute('placeholder').value('Mobile Number'))
    s('#dateOfBirth-label').should(have.text('Date of Birth'))
    s('#dateOfBirthInput').should(have.attribute('value').value(datetime.now().strftime('%d %b %Y')))
    s('#subjectsWrapper').should(have.text('Subjects'))
    s('#hobbiesWrapper').should(have.text('Hobbies'))
    ss('.custom-checkbox').should(have.size(3)).should(have.exact_texts('Sports', 'Reading', 'Music'))
    s('#currentAddress-wrapper').should(have.text('Current Address'))
    s('#currentAddress').should(have.attribute('placeholder').value('Current Address'))
    s('#stateCity-wrapper').should(have.text('State and City'))
