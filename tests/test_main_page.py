from data import *
import pytest
from conftest import *
from selenium import webdriver
from pages.main_page import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import *
from locators.order_page_locators import *

class TestMainPage:

    @pytest.mark.parametrize('num, result', [(0, faq_answer_1),
                             (1, faq_answer_2), (2, faq_answer_3),
                            (3, faq_answer_4), (4, faq_answer_5),
                            (5, faq_answer_6), (6, faq_answer_7),
                            (7, faq_answer_8)], ids=['question_1', 'question_2', 'question_3',
                                 'question_4', 'question_5', 'question_6', 'question_7', 'question_8'])
    def test_questions_and_answer(self, base_page, main_page, webpage, num, result):

        base_page.click_element(MainPageLocators.BUTTON_AGREE_COOKIE)
        main_page.scrool_subheader(MainPageLocators.SUBHEADER_FAQ)

        assert main_page.get_answer_text(MainPageLocators.QUESTION_LOCATOR, MainPageLocators.ANSWER_LOCATOR, num) == result

    def test_logo_scooter(self, webpage, main_page, base_page, order_page):

        base_page.click_element(OrderPageLocations.HEADER_ORDER_BUTTON)
        base_page.click_element(MainPageLocators.HEADER_LOGO_SCOOTER)
        assert base_page.get_text_from_element(MainPageLocators.HOME_PAGE_SCOOTER) == text_header_main_page

    def test_logo_yandex(self, webpage, base_page):

        base_page.click_element(MainPageLocators.HEADER_LOGO_YANDEX)
        assert base_page.switch_to_page(MainPageLocators.YANDEX_DZEN_PAGE) == expected_redirect_url



