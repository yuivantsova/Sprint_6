import allure

from data import *
import pytest
from conftest import *
from selenium import webdriver
from pages.main_page import *
from selenium.webdriver.support import expected_conditions


class TestMainPage:

    @allure.title('Пpоверка блока FAQ')
    @pytest.mark.parametrize('num, result', [(0, faq_answer_1),
                             (1, faq_answer_2), (2, faq_answer_3),
                            (3, faq_answer_4), (4, faq_answer_5),
                            (5, faq_answer_6), (6, faq_answer_7),
                            (7, faq_answer_8)], ids=['question_1', 'question_2', 'question_3',
                                 'question_4', 'question_5', 'question_6', 'question_7', 'question_8'])
    def test_questions_and_answer(self, main_page, webpage, num, result):

        assert main_page.get_answer_text(num) == result

    @allure.title('Проверка, что после нажатия на логотип Самокат попадаешь на главную страницу')
    def test_logo_scooter(self, webpage, main_page):

        assert main_page.logo_scooter() == text_header_main_page

    @allure.title('Проверка, что после нажатия на логотип Яндекс попадешь на страницу Дзен')
    def test_logo_yandex(self, webpage, main_page):

        assert main_page.logo_yandex() == expected_redirect_url



