import allure
import pytest
from selenium import webdriver
from helpers import Urls

@allure.step('Открытие браузера / переход на страницу сервиса / закрытие браузера')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.URL_qa_scooter)
    yield driver
    driver.quit()