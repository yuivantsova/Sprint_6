import allure

from conftest import *
import pytest
from locators.order_page_locators import *
from data import *
from pages.order_page import *


class TestOrderPage:

    @allure.title('Проверка страницы "Для кого заказать"')
    @pytest.mark.parametrize('name, surname, address, station, number_phone, button, result',
                             [(name, surname, address, station, number_phone, OrderPageLocations.HEADER_ORDER_BUTTON, text_header_rent_page),
                              (name, surname, address, station, number_phone, OrderPageLocations.DOWN_ORDER_BUTTON, text_header_rent_page)],
                             ids=['button_header_order', 'button_down_order'])
    def test_order_person_page(self, order_page, name, surname, address, station, number_phone, button, result):

        order_page.click_to_button_order(button)
        order_page.set_order_person_page(name, OrderPageLocations.INPUT_NAME, surname, OrderPageLocations.INPUT_SURNAME, address,
                             OrderPageLocations.INPUT_ADDRESS, station, OrderPageLocations.INPUT_STATION, number_phone,
                             OrderPageLocations.INPUT_PHONE, OrderPageLocations.STATION_LIST, OrderPageLocations.NEXT_BUTTON)
        assert order_page.get_text_from_header_form_2() == result

    @allure.title('Проверка страницы "Про аренду"')
    @pytest.mark.parametrize('name, surname, address, station, number_phone, date, comment, button, result',
                             [(name, surname, address, station, number_phone, date, comment, OrderPageLocations.HEADER_ORDER_BUTTON, text_success_order),
                              (name, surname, address, station, number_phone, date, comment, OrderPageLocations.DOWN_ORDER_BUTTON, text_success_order)],
                             ids=['button_header_order', 'button_down_order'])
    def test_order_rent_page(self, order_page, name, surname, address, station, number_phone, date, comment, button, result):

        order_page.click_to_button_order(button)
        order_page.set_order_person_page(name, OrderPageLocations.INPUT_NAME, surname, OrderPageLocations.INPUT_SURNAME, address,
                             OrderPageLocations.INPUT_ADDRESS, station, OrderPageLocations.INPUT_STATION, number_phone,
                             OrderPageLocations.INPUT_PHONE, OrderPageLocations.STATION_LIST, OrderPageLocations.NEXT_BUTTON)
        order_page.set_order_rent_page(date, OrderPageLocations.INPUT_DATE_DELIVERY,OrderPageLocations.DAY_TEXT,
                             OrderPageLocations.INPUT_RENTAL_TIME, OrderPageLocations.RENTAL_TIME, OrderPageLocations.CHECK_BOX_COLOR,
                             comment, OrderPageLocations.INPUT_COMMENT, OrderPageLocations.FINISH_ORDER_BUTTON,
                             OrderPageLocations.AGREE_BUTTON)
        assert order_page.get_text_from_button_finish() == result






