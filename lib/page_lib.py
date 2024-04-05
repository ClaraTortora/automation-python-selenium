from pages.product_page import ProductPage


class PageLib:
    def __init__(self, driver):
        self.product_page = ProductPage(driver)
