from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.action import Action


class GetText(Action):

    def from_element(self, element, timeout=10):
        try:
            wait = WebDriverWait(self._driver, timeout)
            element = wait.until(EC.visibility_of_element_located(element))
            return element.text
        except (TimeoutException, NoSuchElementException) as e:
            # Handle exception based on your specific needs
            # You can log the error, retry the action, or raise a custom exception
            print(f"Error getting text from element: {e}")
