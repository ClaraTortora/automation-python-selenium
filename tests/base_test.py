from selenium import webdriver

from lib.action_lib import ActionLib
from lib.page_lib import PageLib


class BaseTest:
    def setup(self):
        self._driver = webdriver.Chrome()
        self._actions_lib = ActionLib(self._driver)
        self._pages_lib = PageLib(self._driver)

    def tear_down(self):
        self._driver.quit()
