from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
	def should_not_be_basket_summary(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), \
           "basket summary is presented, but should not be"

	def should_be_empty_basket(self):
		assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
           "empty basket is not presented"