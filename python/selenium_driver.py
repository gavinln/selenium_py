from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# create locators for find_by_name, find_by_id, ...
def find_by_name(name):
    def driver_find_by_name(driver):
        return driver.find_element_by_name(name)
    return driver_find_by_name

# Mapping from program defined values to page defined values
locators = {}
locators['python.search'] = find_by_name('q')
locators['python.submit'] = find_by_name('submit')

class Element(object):
    def __init__(self, locator):
        self.locator = locator
    def __get__(self, instance, owner):
        element = self.locator(instance.driver)
        return element
    def __set__(self, instance, value):
        element = self.locator(instance.driver)
        element.send_keys(value)

class SubmitElement(Element):
    def __init__(self):
        super(SubmitElement, self).__init__(locators['python.submit'])

class PythonPage(object):
    search = Element(locators['python.search'])
    submit = SubmitElement()
    def __init__(self, driver):
        self.driver = driver
        assert "Python" in driver.title

class SearchResultsPage(object):
    def __init__(self, driver):
        self.driver = driver
        assert "Google" in driver.title

#driver = webdriver.Firefox()
driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)

driver.get("http://www.python.org")
pythonPage = PythonPage(driver)
pythonPage.search = "selenium"
pythonPage.submit.click()

searchResults = SearchResultsPage(driver)
driver.close()

