import pytest

from data.dictionary import Route, Size, Color
from tests.base_test import BaseTest
from ui.header_cart_ui import HeaderCartUI
from ui.product_ui import ProductUI


class TestAddToCart(BaseTest):
    def test_given_user_in_home_when_add_to_cart_selecting_options_then_product_is_added_into_cart(self):
        self.setup()
        self._actions_lib.navigate.to_url(Route.HOME)
        self._pages_lib.product_page.select_size('1', Size.XS)
        self._pages_lib.product_page.select_color('1', Color.BLUE)
        self._pages_lib.product_page.add_to_cart('1')
        assert self._actions_lib.get_text.from_element(HeaderCartUI.get_selector_cart_quantity()) == '1'
        self.tear_down()
