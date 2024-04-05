from selenium.webdriver.common.by import By

from pages.page import Page
from ui.product_ui import ProductUI


class ProductPage(Page):

    def add_to_cart(self, item_position):
        self._action_lib.click.wait_and_click(ProductUI.get_selector_add_to_cart_button(item_position))

    def select_color(self, item_position, color):
        self._action_lib.click.wait_and_click(ProductUI.get_selector_color_button(item_position, color))

    def select_size(self, item_position, size):
        self._action_lib.click.wait_and_click(ProductUI.get_selector_size_button(item_position, size))


