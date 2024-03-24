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
    def set_order_person_page(self, name, name_locator, surname, surname_locator, address, address_locator, station,
                  station_locator, number_phone, number_phone_locator, station_list_locator, button_next):
        self.input_text_to_element(name_locator, name)
        self.input_text_to_element(surname_locator, surname)
        self.input_text_to_element(address_locator, address)
        self.input_text_to_element(station_locator, station)
        self.click_element(station_list_locator)
        self.input_text_to_element(number_phone_locator, number_phone)
        self.click_element(button_next)

    @allure.step('Получение текста заголовка Про аренду')
    def get_text_from_header_form_2(self):
        return self.get_text_from_element(OrderPageLocations.HEADER_RENT_PAGE)

    @allure.step('Заполнение полей на странице Про аренду')
    def set_order_rent_page(self, date, date_locator, day_locator, days, days_locator, color_locator, comment, comment_locator,
                  final_order_button, agree_order_locator):

        self.input_text_to_element(date_locator, date)
        self.click_element(day_locator)
        self.click_element(days)
        self.click_element(days_locator)
        self.click_element(color_locator)
        self.input_text_to_element(comment_locator, comment)
        self.click_element(final_order_button)
        self.click_element(agree_order_locator)

    @allure.step('Получение текста с кнопки Посмотреть статус')
    def get_text_from_button_finish(self):
        return self.get_text_from_element(OrderPageLocations.CHECK_ORDER)
