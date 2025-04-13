from pages.base_page import *
from locators.dzen_page_locators import *
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DzenPage(BasePage):

    @allure.step('Проверка отображения на странице дзена кнопки "Главная" ')
    def check_dzen_element_main_button(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(LocatorsDzen.main_button_dzen))
