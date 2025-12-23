import random
import string
import time


def test_1(page):
    day = "22"
    year = "1914"
    month = "5"
    first_name_field_loc = "input#firstName"
    last_name_field_loc = "input#lastName"
    email_field_loc = "input#userEmail"
    button_submit_loc = "button#submit"
    submit_text_loc = "div#example-modal-sizes-title-lg"
    male_radio_button_loc = "label[for='gender-radio-1']"
    female_radio_button_loc = "label[for='gender-radio-2']"
    tel_number_loc = "input#userNumber"
    calendar_date_loc = "input#dateOfBirthInput"
    month_date_loc = "select.react-datepicker__month-select"
    year_date_loc = "select.react-datepicker__year-select"
    day_date_loc = "div[class*='--0"+day+"']"

    names= [''.join(random.choices(string.ascii_lowercase, k=6)) ]
    for first_name in names:
        last_name = "Ivanova"
        email = first_name + "@dd.com"
        submit_text = "Thanks for submitting the form"
        tel_number = "1111111111"


        page.goto("https://demoqa.com/automation-practice-form")
        page.fill(first_name_field_loc, first_name)
        page.fill(last_name_field_loc, last_name)
        page.fill(email_field_loc, email)
        page.locator(male_radio_button_loc).check()
        page.locator(female_radio_button_loc).click()
        page.fill(tel_number_loc, tel_number)
        page.click(calendar_date_loc)
        #page.fill(calendar_date_loc, date)
        page.select_option(month_date_loc, value = month)
        page.select_option(year_date_loc, value = year)
        page.click(day_date_loc)
        time.sleep(2)



        page.click(button_submit_loc)
        text = page.locator(submit_text_loc).text_content()
        print(text)
        assert text == submit_text, "Текст не найден"







