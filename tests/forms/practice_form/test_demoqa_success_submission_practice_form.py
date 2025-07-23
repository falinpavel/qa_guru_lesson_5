import os
from selene import browser, have, be, command
from selene.core.condition import Condition


"""
Путь к загружаемому файлу для теста
"""
UPLOADED_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file.txt")


def test_success_submission_students_registration_form():
    """
    1. Открыть страницу "https://demoqa.com/automation-practice-form"
    2. Заполнить форму:
        1.1. Поле "Name": Ivan
        1.2. Поле "LastName": Ivanov
        1.3. Поле "User" Email: test@example.com
        1.4. Поле "Gender": Male
        1.5. Поле "Mobile": 88002556535
        1.6. Поле "Date of Birth": 23 May,1996
        1.7. Поле "Subjects": Computer Science, Maths, Physics, Biology
        1.8. Поле "Hobbies": Click Sports, Reading, Music (all checkboxes)
        1.9. Поле "Picture": load file.txt from utils dir
        1.10. Поле "Current Address": Moscow
        1.11. Поле "State": Uttar
        1.12. Поле "City": Pradesh Lucknow
    3. Нажать кнопку "Submit"
    4. Проверить, что форма заполнена и данные матчатся в табличке,
     проверяем построчно ключ - значение
    5. Нажать кнопку "Close"
    """
    browser.element('#firstName').should(be.blank).type('Ivan').should(be.not_.blank).should(
        have.attribute("value").value('Ivan'))
    browser.element('#lastName').should(be.blank).type('Ivanov').should(be.not_.blank).should(
        have.attribute("value").value('Ivanov'))
    browser.element('#userEmail').should(be.blank).type('test@example.com').should(be.not_.blank).should(
        have.attribute("value").value('test@example.com'))
    browser.all('[name=gender]').element_by(
        have.attribute('value').value('Male')).element('..').click().should(be.enabled)
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


def test_successful_completion_table():
    """
    Проверки корректного заполнения формы,
     матчим ключи и значения построчно
    """
    test_success_submission_students_registration_form()
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
    """
    1. Открыть страницу https://demoqa.com/automation-practice-form
    2. Не заполняя формы скролить до кнопки "Submit"
    3. Нажать кнопку "Submit"
    4. Проверить что модальное окно "Thanks for submitting the form" не появляется,
         т.е. прошла проверка на обязательность полей
    """
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(be.absent)


def test_check_texts_on_form():
    """
    Проверяем тексты на форме
    """
    browser.element('.practice-form-wrapper').with_(timeout=browser.config.timeout*2).should(
        Condition.by_and(
            have.text('Practice Form'), have.text('Student Registration Form')
        )
    )
    browser.element('#userName-wrapper').should(have.exact_text('Name'))
    browser.element('#userEmail-wrapper').should(have.exact_text('Email'))
    browser.element('#genterWrapper').should(have.text('Gender'))
    browser.element('#userNumber-label').should(
        Condition.by_and(
            have.text('Mobile'), have.text('(10 Digits)')
        )
    )
    browser.element('#userNumber').should(have.attribute('placeholder').value('Mobile Number'))
    browser.element('#dateOfBirth-label').should(have.text('Date of Birth'))
    browser.element('#subjectsWrapper').should(have.text('Subjects'))
    browser.element('#hobbiesWrapper').should(have.text('Hobbies'))
    browser.element('#currentAddress-wrapper').should(have.text('Current Address'))
    browser.element('#stateCity-wrapper').should(have.text('State and City'))
