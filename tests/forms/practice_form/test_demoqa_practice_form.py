from selene import browser, have, be
from selene.core.condition import Condition


def test_successful_filling_students_registration_form():
    browser.open('/automation-practice-form')
    browser.element('.practice-form-wrapper').with_(timeout=browser.config.timeout*2).should(
        Condition.by_and(
            have.text('Practice Form'), have.text('Student Registration Form')
        )
    )
    browser.element('#userName-wrapper').should(have.text('Name'))
    browser.element('#firstName').should(be.blank).type('Ivan').should(have.value('Ivan'))
    browser.element('#lastName').should(be.blank).type('Ivanov').should(have.value('Ivanov'))
    browser.element('#userEmail-wrapper').should(have.text('Email'))
    browser.element('#userEmail').should(be.blank).type('test@example.com').should(have.value('test@example.com'))
    browser.element('#genterWrapper').should(have.text('Gender'))
    gender_elements = browser.all('label[class="custom-control-label"]')
    gender_elements[0].should(have.text('Male')).click()
    gender_elements[1].should(have.text('Female')).click()
    gender_elements[2].should(have.text('Other')).click()
    browser.element('#userNumber-label').should(
        Condition.by_and(
            have.text('Mobile'), have.text('(10 Digits)')
        )
    )
    browser.element('#userNumber').should(be.blank).type('88002556535')
    browser.element('#dateOfBirth-label').should(have.text('Date of Birth'))
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="4"]').with_(timeout=browser.config.timeout*2).should(be.visible).click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1996"]').with_(timeout=browser.config.timeout*2).should(be.visible).click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('div[aria-label="Choose Thursday, May 23rd, 1996"]').click()
    browser.element('#subjectsWrapper').should(have.text('Subjects'))
    subjects_field = browser.element('#subjectsInput')
    subjects_field.type('Computer Science').should(have.value('Computer Science')).press_enter()
    subjects_field.type('Maths').should(have.value('Maths')).press_enter()
    subjects_field.type('Physics').should(have.value('Physics')).press_enter()
    subjects_field.type('Bio').should(have.value('Bio')).press_enter()
    browser.element('#hobbiesWrapper').should(have.text('Hobbies'))
    hobbies_elements = browser.all('label[class="custom-control-label"]')
    hobbies_elements[3].should(have.text('Sports')).click()
    hobbies_elements[4].should(have.text('Reading')).click()
    hobbies_elements[5].should(have.text('Music')).click()
    # TODO! Form for "Pictures"
    browser.element('#currentAddress-wrapper').should(have.text('Current Address'))
    browser.element('#currentAddress').should(be.blank).type('Moscow')
    browser.element('#stateCity-wrapper').should(have.text('State and City'))
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()

