from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.action import Action


class Navigate(Action):

    def to_url(self, url):
        self._driver.get(url)
