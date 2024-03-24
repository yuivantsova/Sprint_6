import allure

from locators.main_page_locators import *
from locators.order_page_locators import *
from pages.base_pages import BasePage


class MainPage(BasePage):

    @allure.step('Получение текста ответа')
    def get_answer_text(self, num):
        self.click_element(MainPageLocators.BUTTON_AGREE_COOKIE)
        self.scrool_to_element(MainPageLocators.SUBHEADER_FAQ)
        locator_que_formated = self.format_locator(MainPageLocators.QUESTION_LOCATOR, num)
        locator_ans_formated = self.format_locator(MainPageLocators.ANSWER_LOCATOR, num)
        self.click_element(locator_que_formated)
        return self.get_text_from_element(locator_ans_formated)

    @allure.step('Переход на вкладку Яндекс.Дзен')
    def logo_yandex(self):

        self.click_element(MainPageLocators.HEADER_LOGO_YANDEX)
        return self.switch_to_page(MainPageLocators.YANDEX_DZEN_PAGE)

    @allure.step('Переход на главную страницу Яндекс.Самокат')
    def logo_scooter(self):

        self.click_element(OrderPageLocations.HEADER_ORDER_BUTTON)
        self.click_element(MainPageLocators.HEADER_LOGO_SCOOTER)
        return self.get_text_from_element(MainPageLocators.HOME_PAGE_SCOOTER)

