import os
from selene.support.shared import browser
from selene import be, have



def test_fill_form(open_browser):
    browser.open('/automation-practice-form')
    brel = browser.element
    brel('[id="firstName"]').should(be.blank).type('Гурбангулы')
    brel('[id="lastName"]').should(be.blank).type('Бердымухамедов')
    brel('[id="userEmail"]').should(be.blank).type('mail@mail.com')
    brel('[for="gender-radio-2"]').click()
    brel('[id="userNumber"]').should(be.blank).type('123456789010')
    brel('[id="dateOfBirthInput"]').click()
    brel('.react-datepicker__month-select>[value="6"]').click()
    brel('.react-datepicker__year-select>[value="1956"]').click()
    brel('.react-datepicker__day--007').click()
    brel('[id="subjectsInput"]').type("Maths").press_enter()
    brel('[for="hobbies-checkbox-2"]').click()
    brel('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), '../files/img.png')))
    brel('[id="currentAddress"]').should(be.blank).type('Троллоло стрит')
    brel("#state").click()
    brel("#react-select-3-input").type('Uttar Pradesh').press_enter()
    brel("#city").click()
    brel("#react-select-4-input").type('Agra').press_enter()
    brel('[type="submit"]').click()
    brel('.table-responsive').should(have.text('Гурбангулы Бердымухамедов'))
    brel('.table-responsive').should(have.text('mail@mail.com'))
    brel('.table-responsive').should(have.text('Female'))
    brel('.table-responsive').should(have.text('1234567890'))
    brel('.table-responsive').should(have.text('07 July,1956'))
    brel('.table-responsive').should(have.text('img.png'))
    brel('.table-responsive').should(have.text('Троллоло стрит'))
    brel('.table-responsive').should(have.text('Uttar Pradesh Agra'))

