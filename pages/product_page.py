from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage): 
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()
        self.should_be_product_name()
        self.should_be_product_price()

    def should_be_product_name(self):
        product_name = str(self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text)
        alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        assert product_name == alert_product_name, "product name is not presented"

    def should_be_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_product_price = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text
        assert product_price == alert_product_price, "product price is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "success message is presented, but should not be"

    def success_message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "success message is not disappeared, but should be"
