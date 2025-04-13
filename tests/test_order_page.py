import allure

from helpers import *
from pages.home_page import *
from pages.order_page import *


class TestOrderPage:

    @allure.title('Позитивный тест оформления заказа')
    def test_order_scooter_success(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.scroll_and_click_on_the_order_button()
        order_page.order_scooter_full_path(Users.user_2)
        assert order_page.check_order_title()
