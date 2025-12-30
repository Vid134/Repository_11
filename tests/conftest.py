import pytest     ##this imports the pytest framework so that we can use fixtures
from selenium import webdriver     ##imports the webdriver module from

##Fixture provides setup and teardown for tests
@pytest.fixture
def driver():          ##definition of a fixture function
    driver = webdriver.Chrome()      ##creates chrome browser instance using selenium webdriver
    driver.maximize_window()         ##maximizes the browser window
    driver.get("https://classify.zenclass.in/")     ##opens the url in the chrome browser
    yield driver    ##yield provides the driver to test, before yield :setup code(browser launch), After yield: Teardown code (what happens after test finishes)
    driver.quit()     ##browser closes

