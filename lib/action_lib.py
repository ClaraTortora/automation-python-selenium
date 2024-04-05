from actions.click import Click
from actions.get_text import GetText
from actions.navigate import Navigate


class ActionLib:
    def __init__(self, driver):
        self.click = Click(driver)
        self.navigate = Navigate(driver)
        self.get_text = GetText(driver)