from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.action import Action


class Click(Action):

    def wait_and_click(self, element, timeout=10):
        try:
            wait = WebDriverWait(self._driver, timeout)
            wait.until(EC.element_to_be_clickable(element)).click()
        except (TimeoutException, NoSuchElementException) as e:
            # Handle exception based on your specific needs
            # You can log the error, retry the action, or raise a custom exception
            print(f"Error clicking element: {e}")
