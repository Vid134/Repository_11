from selenium.webdriver.common.by import By  ##importing selenium modules which allows identifying elements
from selenium.webdriver.support.ui import WebDriverWait  ##imports used to apply explicit waits
from selenium.webdriver.support import expected_conditions as EC  ##expected comditions for waits

class LoginPage:    ##Page object model class for login page

    def __init__(self, driver):
        self.driver = driver   #assigns driver instance for class usage
        self.wait = WebDriverWait(driver, 10)  #Explicit wait with timeout 10sec

     ####Locators------

    username_input = (By.ID,"useremail")  ##locator for email input box
    password_input = (By.ID,"password")   ##locator for password input box
    login_button_submit = (By.ID,"loginBtn")  ##locator for login button
    error_message = (By.ID,"toastContainer")  ##locator for invalid login error

    ##Actions---------

    def enter_username(self,username:str) -> None:
        username_field = self.wait.until(                ##wait until email field becomes clickable
            EC.element_to_be_clickable(self.username_input)
        )
        username_field.clear()                             ##clears the prefilled text if any
        username_field.send_keys(username)       ##Enters username value into input field

    def enter_password(self,password:str) -> None:
        password_field = self.wait.until(                  ##wait until password becomes clickable
            EC.element_to_be_clickable(self.password_input)
        )
        password_field.clear()                               ##clears the prefilled text if any
        password_field.send_keys(password)                     ##Enters password value into input field

##UI Validation method------------

    def is_username_input_visible(self):
        return self.wait.until(                                ##wait until username is visible
            EC.visibility_of_element_located(self.username_input)
        ).is_displayed()                                         ##return true if visible

    def is_password_input_visible(self):
        return self.wait.until(                                   ##wait until password is visible
            EC.visibility_of_element_located(self.password_input)
        ).is_displayed()                                            ##return true if visible

    def is_login_button_clickable(self):
        try:
            self.wait.until(                                             ##wait until login button is clickable
                EC.element_to_be_clickable(self.login_button_submit)
            )
            return True                                            ##button is clickable
        except:
            return False                                           ##but not ready ,if wait fails

##Login submit----------------

    def click_login(self) -> None:
        login_button = self.wait.until(                   #wait until login button becomes clickable
            EC.element_to_be_clickable(self.login_button_submit)
        )
        login_button.click()                               ## Click login button

##Error message--------------------

    def get_error_login(self) -> None:
        error_msg = self.wait.until(                        ##wait until error message appears
                EC.visibility_of_element_located(self.error_message)
        )
        return error_msg.text                               ##returns error message text
