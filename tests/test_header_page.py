import time
import allure
import pytest

from helpers import *
from locators.home_page_locators import *
from pages.home_page import *
from pages.dzen_page import *


class TestMainPage:

    @allure.title('Позитивный тест проверки перехода на главную страницу при клике на логотип "Самокат"')
    def test_scooter_logo_click(self, driver):
        header_page = HomePage(driver)
        header_page.order_button_click()
        header_page.scooter_logo_click()
        current_url = header_page.get_current_url()
        title_is_displayed = header_page.check_order_title()
        assert current_url == Urls.URL_qa_scooter and title_is_displayed

    @allure.title('Позитивный тест проверки перехода на главную страницу дзен при клике на логотип "Яндекс"')
    def test_yandex_logo_click(self, driver):
        header_page = HomePage(driver)
        dzen_page = DzenPage(driver)
        header_page.yandex_logo_click()
        header_page.go_to_new_tab()
        #time.sleep(5)
        # Убрал sleep и добавил функцию ожидания открытия с expected_condition в базовый класс
        header_page.wait_dzen(Urls.URL_dzen)
        current_url = header_page.get_current_url()
        assert current_url == Urls.URL_dzen and dzen_page.check_dzen_element_main_button()

    @allure.title('Позитивный тест проверки текста ответов на вопросы на главной странице веб-приложения')
    @pytest.mark.parametrize('question_locator, question_text_locator, expected_answer', zip(LocatorsHome.questions, LocatorsHome.questions_text, Questions.expected_question_text))
    def test_quest_answer(self, driver, question_locator, question_text_locator, expected_answer):
        home_page = HomePage(driver)
        text = home_page.get_text_question(question_locator, question_text_locator)
        assert text == expected_answer
