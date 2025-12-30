from pages.login_page import LoginPage    ##Imports the Loginpage class from the page object folder
from pages.logout_page import logoutPage    ##Imports the Logoutpage class from the page object folder

##Testcase for logout
##defines the test for logout functionality
def test_logout_functionality(driver):
    login = LoginPage(driver)                  ##creates an object of loginpage passing the webdriver to interact with login elements
    logout = logoutPage(driver)                ##creates an object of logoutpage passing the webdriver to interact with logout elements

    # Login first
    login.enter_username("vidhya.venkruk@gmail.com")   ##enters the username field with valid username
    login.enter_password("Ganesha@2021")                     ##enters the password field with valid password
    login.click_login()                                 ##click the loginbutton

    # Perform logout
    logout.click_account_pop_button()         ##to click account pop button
    logout.click_signout_button()             ##to click signout button

    # validate success logout message

    assert "classify"  in driver.current_url.lower()
##asserting because this verifies logout is succesful by checking page url contains classify as it is in the login page now


