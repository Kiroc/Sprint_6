# Финальный проект 6 спринта "Page Object"
## Файлы:
- conftest.py - файл с фикстурами
- helpers.py - файл со вспомогательными данными
- pages/ - каталог с файлами страниц
- - pages/base_page.py - файл с базовыми методами взаимодействия с элементами
- - pages/home_page.py -  файл с методами взаимодействия с домашней страницей
- - pages/order_page.py - файл с методами взаимодействия со страницами оформления заказа
- locators/ - каталог с файлами локаторов страниц
- - locators/home_page_locators.py - файл с локаторами элементов на домашней страницы
- - locators/order_page_locators.py - файл с локаторами элементов на страницах оформления заказа
- tests/ - каталог с автотестами
- - tests/test_home_page.py - файл с проверками домашней страницы 
- - tests/test_order_page.py - файл с проверками оформления заказа
- requirements.txt - файл с внешними зависимостями
- allure_results - каталог с отчетом о тестировании
Установить зависимости 
```shell
pip install -r requirements.txt
```
Запустить все тесты
```shell
python -m pytest --alluredir allure-results
```
Посмотреть отчет
```shell
python -m allure serve allure_results
```
