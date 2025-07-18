from selene import browser, have, be
from selene.core.condition import Condition


def test_filling_students_registration_form():
    browser.open('/automation-practice-form')
    browser.element('.practice-form-wrapper').with_(timeout=browser.config.timeout*2).should(
        Condition.by_and(
            have.text('Practice Form'), have.text('Student Registration Form')
        )
    )
    browser.element('#userName-wrapper').should(have.text('Name'))
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail-wrapper').should(have.text('Email'))
    browser.element('#userEmail').type('N5YF2@example.com')
    browser.element('#genterWrapper').should(have.text('Gender'))
    gender_elements = browser.all('label[class="custom-control-label"]')
    gender_elements[0].should(have.text('Male')).click()
    gender_elements[1].should(have.text('Female')).click()
    gender_elements[2].should(have.text('Other')).click()

