import time

from pages.base_pages import BasePage


class MainPage(BasePage):

    def scrool_subheader(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_answer_text(self, locator_que, locator_ans, num):
        locator_que_formated = self.format_locator(locator_que, num)
        locator_ans_formated = self.format_locator(locator_ans, num)
        self.click_element(locator_que_formated)
        return self.get_text_from_element(locator_ans_formated)
