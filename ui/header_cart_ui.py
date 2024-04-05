from selenium.webdriver.common.by import By

from data.dictionary import Color, Size


class HeaderCartUI:
    @staticmethod
    def get_selector_cart_quantity():
        return By.XPATH, '//a[@class="action showcart"]//child::span[@class="counter-number"]'
