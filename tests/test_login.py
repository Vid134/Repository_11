import pytest         ##imports the pytest framework to run the automated tests
from pages.login_page import LoginPage    ##Imports the Loginpage class from the page object folder

##Testcase1
##Defines a test function using the driver fixture
def test_successful_login(driver):
    login = LoginPage(driver)    ##creates an object og loginpage passing the webdriver to interact with login elements
    login.enter_username("vidhya.venkruk@gmail.com")  ##enters the username field with valid username
    login.enter_password("Ganesha@2021")               ##enters the password field with valid password
    login.click_login()                                 ##clicks on the login button

    # After successful login, login button should not be visible OR redirected
    assert "classify" in driver.current_url.lower()  ##asserting because this verifies login is succesful by checking page url contains classify

##Testcase2 : Negative----------
##defines the  test function for negative login case
def test_unsuccessful_login(driver):
    login = LoginPage(driver)     ##creates an object og loginpage passing the webdriver to interact with login elements
    login.enter_username("wronguser@gmail.com")    ##enters the username field with invalid username
    login.enter_password("wrongpass")                   ##enters the password field with invalid password
    login.click_login()                                     ##clicks on the login button

    error_text = login.get_error_login()              ##calls a method to capture login error text displayed on ui
    assert "incorrect" in error_text.lower()          ##verifies error message contains incorrect ,as login failed

##Testcase3
##defines the test to check input fields are visible in the ui
def test_input_fields_visible(driver):
    login = LoginPage(driver)             ##creates an object og loginpage passing the webdriver to interact with login element

    assert login.is_username_input_visible() is True    ##confirms username input box is present and visible
    assert login.is_password_input_visible() is True         ##confirms password input box is present and visible

##testcase4
##validates login button ui behaviour
def test_login_button_clickable(driver):
    login = LoginPage(driver)                 ##creates an object og loginpage passing the webdriver to interact with login element

    assert login.is_login_button_clickable() is True     #checks whether the login button is clickable

