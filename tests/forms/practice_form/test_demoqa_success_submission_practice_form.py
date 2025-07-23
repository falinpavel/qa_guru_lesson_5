import os
from selene import browser, have, be
from datetime import datetime


UPLOADED_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file.txt")


def test_successful_filling_students_registration_form():
    browser.element('#firstName').should(be.blank).type('Ivan').should(be.not_.blank).should(
        have.attribute("value").value('Ivan'))
    browser.element('#lastName').should(be.blank).type('Ivanov').should(be.not_.blank).should(
        have.attribute("value").value('Ivanov'))
    browser.element('#userEmail').should(be.blank).type('test@example.com').should(be.not_.blank).should(
        have.attribute("value").value('test@example.com'))
    browser.element('label[for="gender-radio-1"]').click().should(be.enabled)
    browser.element('#userNumber').should(be.blank).send_keys('8800255653').should(be.not_.blank).should(
        have.attribute("value").value('8800255653'))
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="4"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1996"]').click()
    browser.element('div[aria-label="Choose Thursday, May 23rd, 1996"]').click()
    browser.element('#dateOfBirthInput').should(be.not_.blank).should(have.attribute("value").value('23 May 1996'))
    browser.element('#subjectsInput').type('Computer Science').should(
        have.attribute("value").value('Computer Science')).press_enter()
    browser.all('label[class="custom-control-label"]').element_by(have.text('Sports')).click().should(be.enabled)
    browser.element('#uploadPicture').send_keys(os.path.abspath(UPLOADED_FILE))
    browser.element('#currentAddress').should(be.blank).type('Moscow').should(be.not_.blank).should(
        have.attribute("value").value('Moscow'))
    browser.element('#state').click().element('#react-select-3-option-1').click()
    browser.element('#city').click().element('#react-select-4-option-1').click()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))


def test_successful_filling_table():
    test_success_filling_students_registration_form()
    table_element = browser.all('table.table-dark tbody tr')
    table_element.element_by(have.text('Student Name')).all('td').second.should(have.text('Ivan Ivanov'))
    table_element.element_by(have.text('Student Email')).all('td').second.should(have.text('test@example.com'))
    table_element.element_by(have.text('Gender')).all('td').second.should(have.text('Male'))
    table_element.element_by(have.text('Mobile')).all('td').second.should(have.text('8800255653'))
    table_element.element_by(have.text('Date of Birth')).all('td').second.should(have.text('23 May,1996'))
    table_element.element_by(have.text('Subjects')).all('td').second.should(have.text('Computer Science'))
    table_element.element_by(have.text('Hobbies')).all('td').second.should(have.text('Sports'))
    table_element.element_by(have.text('Picture')).all('td').second.should(have.text('file.txt'))
    table_element.element_by(have.text('Address')).all('td').second.should(have.text('Moscow'))
    table_element.element_by(have.text('State and City')).all('td').second.should(have.text('Uttar Pradesh Lucknow'))


def test_submission_form_with_empty_fields():
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(be.absent)


def test_check_texts_on_form():
    browser.element('.text-center').should(have.text('Practice Form'))
    browser.element('.practice-form-wrapper h5').should(have.text('Student Registration Form'))
    browser.element('#userName-wrapper').should(have.exact_text('Name'))
    browser.element('#firstName').should(have.attribute('placeholder').value('First Name'))
    browser.element('#lastName').should(have.attribute('placeholder').value('Last Name'))
    browser.element('#genterWrapper').should(have.text('Gender'))
    browser.all('.custom-radio').should(have.size(3)).should(have.exact_texts('Male', 'Female', 'Other'))
    browser.element('#userNumber-label').should(have.text('Mobile')).element('small').should(have.text('(10 Digits)'))
    browser.element('#userNumber').should(have.attribute('placeholder').value('Mobile Number'))
    browser.element('#dateOfBirth-label').should(have.text('Date of Birth'))
    browser.element('#dateOfBirthInput').should(have.attribute('value').value(datetime.now().strftime('%d %b %Y')))
    browser.element('#subjectsWrapper').should(have.text('Subjects'))
    browser.element('#hobbiesWrapper').should(have.text('Hobbies'))
    browser.all('.custom-checkbox').should(have.size(3)).should(have.exact_texts('Sports', 'Reading', 'Music'))
    browser.element('#currentAddress-wrapper').should(have.text('Current Address'))
    browser.element('#currentAddress').should(have.attribute('placeholder').value('Current Address'))
    browser.element('#stateCity-wrapper').should(have.text('State and City'))
