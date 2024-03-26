import allure

from locators.order_page_locators import *
from locators.main_page_locators import *
from pages.base_pages import BasePage


class OrderPage(BasePage):

    @allure.step('Клик по кнопке Заказать')
    def click_to_button_order(self, locator):
        self.click_element(MainPageLocators.BUTTON_AGREE_COOKIE)
        if locator == 'OrderPageLocations.DOWN_ORDER_BUTTON':
            self.scrool_to_element(locator)
            self.click_element(locator)
        else:
            self.click_element(locator)

    @allure.step('Заполнение полей на странице Для кого самокат')
    def set_order_person_page(self, name, surname, address, station, number_phone):
        self.input_text_to_element(OrderPageLocations.INPUT_NAME, name)
        self.input_text_to_element(OrderPageLocations.INPUT_SURNAME, surname)
        self.input_text_to_element(OrderPageLocations.INPUT_ADDRESS, address)
        self.input_text_to_element(OrderPageLocations.INPUT_STATION, station)
        self.click_element(OrderPageLocations.STATION_LIST)
        self.input_text_to_element(OrderPageLocations.INPUT_PHONE, number_phone)
        self.click_element(OrderPageLocations.NEXT_BUTTON)

    @allure.step('Получение текста заголовка Про аренду')
    def get_text_from_header_form_2(self):
        return self.get_text_from_element(OrderPageLocations.HEADER_RENT_PAGE)

    @allure.step('Заполнение полей на странице Про аренду')
    def set_order_rent_page(self, date, comment):

        self.input_text_to_element(OrderPageLocations.INPUT_DATE_DELIVERY, date)
        self.click_element(OrderPageLocations.DAY_TEXT)
        self.click_element(OrderPageLocations.INPUT_RENTAL_TIME)
        self.click_element(OrderPageLocations.RENTAL_TIME)
        self.click_element(OrderPageLocations.CHECK_BOX_COLOR)
        self.input_text_to_element(OrderPageLocations.INPUT_COMMENT, comment)
        self.click_element(OrderPageLocations.FINISH_ORDER_BUTTON)
        self.click_element(OrderPageLocations.AGREE_BUTTON)

    @allure.step('Получение текста с кнопки Посмотреть статус')
    def get_text_from_button_finish(self):
        return self.get_text_from_element(OrderPageLocations.CHECK_ORDER)
