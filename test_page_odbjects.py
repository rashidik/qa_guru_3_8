import os
from selene.support.shared import browser
from selene import be, have



def test_fill_form(open_browser):
    browser.open('/automation-practice-form')
    browser.element('[id="firstName"]').should(be.blank).type('Гурбангулы')
    browser.element('[id="lastName"]').should(be.blank).type('Бердымухамедов')
    browser.element('[id="userEmail"]').should(be.blank).type('mail@mail.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('[id="userNumber"]').should(be.blank).type('123456789010')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select>[value="6"]').click()
    browser.element('.react-datepicker__year-select>[value="1956"]').click()
    browser.element('.react-datepicker__day--007').click()
    browser.element('[id="subjectsInput"]').type("Maths").press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), '../files/img.png')))
    browser.element('[id="currentAddress"]').should(be.blank).type('Троллоло стрит')
    browser.element("#state").click()
    browser.element("#react-select-3-input").type('Uttar Pradesh').press_enter()
    browser.element("#city").click()
    browser.element("#react-select-4-input").type('Agra').press_enter()
    browser.element('[type="submit"]').click()
    browser.element('.table-responsive').should(have.text('Гурбангулы Бердымухамедов'))
    browser.element('.table-responsive').should(have.text('mail@mail.com'))
    browser.element('.table-responsive').should(have.text('Female'))
    browser.element('.table-responsive').should(have.text('1234567890'))
    browser.element('.table-responsive').should(have.text('07 July,1956'))
    browser.element('.table-responsive').should(have.text('img.png'))
    browser.element('.table-responsive').should(have.text('Троллоло стрит'))
    browser.element('.table-responsive').should(have.text('Uttar Pradesh Agra'))

