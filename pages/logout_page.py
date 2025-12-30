from selenium.webdriver.common.by import By      ##importing selenium modules which allows identifying elements
from selenium.webdriver.support.ui import WebDriverWait      ##imports used to apply explicit waits
from selenium.webdriver.support import expected_conditions as EC     ##expected comditions for waits

class logoutPage:      ##Page object model class for logout page

    def __init__(self, driver):
        self.driver = driver                            #assigns driver instance for class usage
        self.wait = WebDriverWait(driver, 10)    #Explicit wait with timeout 10sec


##Locators---------------------------

    account_button = (By.ID,"account-pop-button")         ##locator for account button
    logout_button = (By.ID,"logout")                       ##locator for logout button
    logout_message = (By.ID,"toast-container")              ##locator for logout message

###Actions----------------------------------

    def click_account_pop_button(self) -> None:
        account_pop =  self.wait.until(
            EC.element_to_be_clickable(self.account_button)    ##wait until account button become clickable
        )
        account_pop.click()                                     ##click the account pop button

#### UI validation method--------------------
    def get_logout_message(self) -> str:
        message = self.wait.until(                          ##wait until logout message is visible
            EC.visibility_of_element_located(self.logout_message)
        )
        return message.text                                    ##returns the text

##Logout --------------------

    def click_signout_button(self) -> None:
        signout_btn = self.wait.until(                        ##wait until logout is clickable
            EC.element_to_be_clickable(self.logout_button)
        )
        signout_btn.click()                            ##Click the logout button





