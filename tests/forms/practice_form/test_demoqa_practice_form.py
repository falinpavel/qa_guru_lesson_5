import os
from selene import browser, have, be, command
from selene.core.condition import Condition


"""
Путь к загружаемому файлу для теста
"""
file_path = os.path.join("utils", "file.txt")


def test_successful_filling_students_registration_form():
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
    browser.should(have.title('DEMOQA'))
    browser.element('.practice-form-wrapper').with_(timeout=browser.config.timeout*2).should(
        Condition.by_and(
            have.text('Practice Form'), have.text('Student Registration Form')
        )
    )
    browser.element('#userName-wrapper').should(have.exact_text('Name'))
    browser.element('#firstName').should(be.blank).type('Ivan').should(be.not_.blank).should(have.value('Ivan'))
    browser.element('#lastName').should(be.blank).type('Ivanov').should(be.not_.blank).should(have.value('Ivanov'))
    browser.element('#userEmail-wrapper').should(have.exact_text('Email'))
    browser.element('#userEmail').should(be.blank).type('test@example.com').should(be.not_.blank).should(
        have.value('test@example.com'))
    browser.element('#genterWrapper').should(have.text('Gender'))
    gender_elements = browser.all('label[class="custom-control-label"]')
    gender_elements[0].should(have.text('Male')).click().should(be.enabled)
    gender_elements[1].should(have.text('Female')).click().should(be.enabled)
    gender_elements[2].should(have.text('Other')).click().should(be.enabled)
    browser.element('#userNumber-label').should(
        Condition.by_and(
            have.text('Mobile'), have.text('(10 Digits)')
        )
    )
    browser.element('#userNumber').should(have.attribute('placeholder', 'Mobile Number'))
    browser.element('#userNumber').should(be.blank).send_keys('88002556535').should(be.not_.blank)
    browser.element('#dateOfBirth-label').should(have.text('Date of Birth'))
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="4"]').with_(timeout=browser.config.timeout*2).should(be.visible).click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1996"]').with_(timeout=browser.config.timeout*2).should(be.visible).click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('div[aria-label="Choose Thursday, May 23rd, 1996"]').click()
    browser.element('#dateOfBirthInput').should(be.not_.blank).should(have.value('23 May 1996'))
    browser.element('#subjectsWrapper').should(have.text('Subjects'))
    subjects_field = browser.element('#subjectsInput')
    subjects_field.type('Computer Science').should(have.value('Computer Science')).press_enter()
    subjects_field.type('Maths').should(have.value('Maths')).press_enter()
    subjects_field.type('Physics').should(have.value('Physics')).press_enter()
    subjects_field.type('Bio').should(have.value('Bio')).press_enter()
    browser.element('#hobbiesWrapper').should(have.text('Hobbies'))
    hobbies_elements = browser.all('label[class="custom-control-label"]')
    hobbies_elements[3].should(have.text('Sports')).click().should(be.enabled)
    hobbies_elements[4].should(have.text('Reading')).click().should(be.enabled)
    hobbies_elements[5].should(have.text('Music')).click().should(be.enabled)
    browser.element('#uploadPicture').send_keys(os.path.abspath(file_path))
    browser.element('#currentAddress-wrapper').should(have.text('Current Address'))
    browser.element('#currentAddress').should(be.blank).type('Moscow').should(be.not_.blank).should(
        have.value('Moscow'))
    browser.element('#stateCity-wrapper').perform(command.js.scroll_into_view)
    browser.element('#stateCity-wrapper').should(have.text('State and City'))
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    """
    Далее по коду идут проверки корректного заполнения формы,
     матчим ключи и значения построчно
    """ # TODO! Доделать
    browser.all('table.table-dark tbody tr').element_by(
        have.text('Student Name')).all('td').second.should(have.text('Ivan Ivanov'))
    browser.all('table.table-dark tbody tr').element_by(
        have.text('Student Email')).all('td').second.should(have.text('test@example.com'))
    browser.all('table.table-dark tbody tr').element_by(
        have.text('Gender')).all('td').second.should(have.text('Other'))
    browser.all('table.table-dark tbody tr').element_by(
        have.text('Mobile')).all('td').second.should(have.text('8800255653'))
    browser.all('table.table-dark tbody tr').element_by(
        have.text('Date of Birth')).all('td').second.should(have.text('23 May,1996'))
    browser.all('table.table-dark tbody tr').element_by(
        have.text('Subjects')).all('td').second.should(have.text('Computer Science, Maths, Physics, Biology'))
    browser.all('table.table-dark tbody tr').element_by(
        have.text('Hobbies')).all('td').second.should(have.text('Sports, Reading, Music'))
    browser.all('table.table-dark tbody tr').element_by(
        have.text('Picture')).all('td').second.should(have.text('file.txt'))
    browser.all('table.table-dark tbody tr').element_by(
        have.text('Address')).all('td').second.should(have.text('Moscow'))
    browser.all('table.table-dark tbody tr').element_by(
        have.text('State and City')).all('td').second.should(have.text('Uttar Pradesh Lucknow'))


def test_with_empty_fields():
    """
    1. Открыть страницу https://demoqa.com/automation-practice-form
    2. Не заполняя формы скролить до кнопки "Submit"
    3. Нажать кнопку "Submit"
    4. Проверить что модальное окно "Thanks for submitting the form" не появляется,
         т.е. прошла проверка на обязательность полей
    """
    browser.should(have.title('DEMOQA'))
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(be.absent)
