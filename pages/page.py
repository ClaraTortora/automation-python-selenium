from lib.action_lib import ActionLib


class Page:
    def __init__(self, driver):
        self._driver = driver
        self._action_lib = ActionLib(driver)
