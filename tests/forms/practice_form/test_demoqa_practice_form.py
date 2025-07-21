import os
from selene import browser, have, be, command
from selene.core.condition import Condition
from selene.support.shared.jquery_style import s, ss


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
    browser.element('.practice-form-wrapper').with_(timeout=browser.config.timeout*2).should(
        Condition.by_and(
            have.text('Practice Form'), have.text('Student Registration Form')
        )
    )
    s('#userName-wrapper').should(have.text('Name'))
    s('#firstName').should(be.blank).type('Ivan').should(have.value('Ivan'))
    s('#lastName').should(be.blank).type('Ivanov').should(have.value('Ivanov'))
    s('#userEmail-wrapper').should(have.text('Email'))
    s('#userEmail').should(be.blank).type('test@example.com').should(have.value('test@example.com'))
    s('#genterWrapper').should(have.text('Gender'))
    genders = ss('label[class="custom-control-label"]')
    genders[0].should(have.text('Male')).click()
    genders[1].should(have.text('Female')).click()
    genders[2].should(have.text('Other')).click()
    s('#userNumber-label').should(
        Condition.by_and(
            have.text('Mobile'), have.text('(10 Digits)')
        )
    )
    s('#userNumber').should(be.blank).type('88002556535')
    s('#dateOfBirth-label').should(have.text('Date of Birth'))
    s('#dateOfBirthInput').click()
    s('.react-datepicker__month-select').click()
    s('option[value="4"]').with_(timeout=browser.config.timeout*2).should(be.visible).click()
    s('.react-datepicker__month-select').click()
    s('.react-datepicker__year-select').click()
    s('option[value="1996"]').with_(timeout=browser.config.timeout*2).should(be.visible).click()
    s('.react-datepicker__year-select').click()
    s('div[aria-label="Choose Thursday, May 23rd, 1996"]').click()
    s('#subjectsWrapper').should(have.text('Subjects'))
    subjects = browser.element('#subjectsInput')
    subjects.type('Computer Science').should(have.value('Computer Science')).press_enter()
    subjects.type('Maths').should(have.value('Maths')).press_enter()
    subjects.type('Physics').should(have.value('Physics')).press_enter()
    subjects.type('Bio').should(have.value('Bio')).press_enter()
    browser.element('#hobbiesWrapper').should(have.text('Hobbies'))
    hobbies = ss('label[class="custom-control-label"]')
    hobbies[3].should(have.text('Sports')).click()
    hobbies[4].should(have.text('Reading')).click()
    hobbies[5].should(have.text('Music')).click()
    s('#uploadPicture').send_keys(os.path.abspath(file_path))
    s('#currentAddress-wrapper').should(have.text('Current Address'))
    s('#currentAddress').should(be.blank).type('Moscow')
    s('#stateCity-wrapper').perform(command.js.scroll_into_view)
    s('#stateCity-wrapper').should(have.text('State and City'))
    s('#state').click()
    s('#react-select-3-option-1').click()
    s('#city').click()
    s('#react-select-4-option-1').click()
    s('#submit').click()
    s('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    """
    Далее по коду идут проверки корректного заполнения формы,
     матчим ключи и значения построчно
    """
    ss('table.table-dark tbody tr').element_by(
        have.text('Student Name')).ss('td').second.should(have.text('Ivan Ivanov'))
    ss('table.table-dark tbody tr').element_by(
        have.text('Student Email')).ss('td').second.should(have.text('test@example.com'))
    ss('table.table-dark tbody tr').element_by(
        have.text('Gender')).ss('td').second.should(have.text('Other'))
    ss('table.table-dark tbody tr').element_by(
        have.text('Mobile')).ss('td').second.should(have.text('8800255653'))
    ss('table.table-dark tbody tr').element_by(
        have.text('Date of Birth')).ss('td').second.should(have.text('23 May,1996'))
    ss('table.table-dark tbody tr').element_by(
        have.text('Subjects')).ss('td').second.should(have.text('Computer Science, Maths, Physics, Biology'))
    ss('table.table-dark tbody tr').element_by(
        have.text('Hobbies')).ss('td').second.should(have.text('Sports, Reading, Music'))
    ss('table.table-dark tbody tr').element_by(
        have.text('Picture')).ss('td').second.should(have.text('file.txt'))
    ss('table.table-dark tbody tr').element_by(
        have.text('Address')).ss('td').second.should(have.text('Moscow'))
    ss('table.table-dark tbody tr').element_by(
        have.text('State and City')).ss('td').second.should(have.text('Uttar Pradesh Lucknow'))


def test_with_empty_fields():
    """
    1. Открыть страницу https://demoqa.com/automation-practice-form
    2. Не заполняя формы скролить до кнопки "Submit"
    3. Нажать кнопку "Submit"
    4. Проверить что модальное окно "Thanks for submitting the form" не появляется,
         т.е. прошла проверка на обязательность полей
    """
    s('#submit').perform(command.js.scroll_into_view)
    s('#submit').click()
    s('#example-modal-sizes-title-lg').should(be.absent)
