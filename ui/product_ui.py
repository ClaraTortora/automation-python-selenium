from selenium.webdriver.common.by import By

from data.dictionary import Color, Size


class ProductUI:
    @staticmethod
    def get_selector_add_to_cart_button(item_position):
        return By.XPATH, '(//button[@title = "Add to Cart"])[' + item_position + ']'

    @staticmethod
    def get_selector_size_button(item_position, size):
        return By.XPATH, '(//button[@title = "Add to Cart"])[' + item_position + ']//preceding::div[@option-label = "' + size + '"]'

    @staticmethod
    def get_selector_color_button(item_position, color):
        return By.XPATH, '(//button[@title = "Add to Cart"])[' + item_position + ']//preceding::div[@option-label = "' + color + '"]'
