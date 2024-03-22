from conftest import *
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import *
from locators.order_page_locators import *
from data import *
from pages.order_page import *
from pages.main_page import *


class TestOrderPage:

    @pytest.mark.parametrize('name, surname, address, station, number_phone, date, comment, button, result',
                             [(name, surname, address, station, number_phone, date, comment, OrderPageLocations.HEADER_ORDER_BUTTON, text_success_order),
                              (name, surname, address, station, number_phone, date, comment, OrderPageLocations.DOWN_ORDER_BUTTON, text_success_order)],
                             ids=['button_header_order', 'button_down_order'])
    def test_order(self, main_page, base_page,order_page, webpage, name, surname, address, station, number_phone, date, comment, button, result):

        base_page.click_element(MainPageLocators.BUTTON_AGREE_COOKIE)

        if button == 'OrderPageLocations.DOWN_ORDER_BUTTON':
            main_page.scrool_subheader(OrderPageLocations)
            base_page.click_element(button)
        else:
            base_page.click_element(button)

        order_page.set_order(name, OrderPageLocations.INPUT_NAME, surname, OrderPageLocations.INPUT_SURNAME, address,
                             OrderPageLocations.INPUT_ADDRESS, station, OrderPageLocations.INPUT_STATION, number_phone,
                             OrderPageLocations.INPUT_PHONE, OrderPageLocations.STATION_LIST, OrderPageLocations.NEXT_BUTTON,
                             date, OrderPageLocations.INPUT_DATE_DELIVERY,OrderPageLocations.DAY_TEXT,
                             OrderPageLocations.INPUT_RENTAL_TIME, OrderPageLocations.RENTAL_TIME, OrderPageLocations.CHECK_BOX_COLOR,
                             comment, OrderPageLocations.INPUT_COMMENT, OrderPageLocations.FINISH_ORDER_BUTTON,
                             OrderPageLocations.AGREE_BUTTON)

        assert base_page.get_text_from_element(OrderPageLocations.CHECK_ORDER) == result





