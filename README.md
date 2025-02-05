## Дипломный проект. Задание 2: API тесты

### Автотесты для проверки работоспособности веб-сервиса Stellar Burgers

### Реализованные сценарии

Созданы API-тесты, покрывающие классы `UserMethods`, `OrderMethods`


### Структура проекта

- `methods` - пакет, содержащий реализованные методы, разбитые на `user_methods.py` и `order_methods.py`
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `test_create_user.py`, `test_login_user.py`, `test_change_user_data.py`',
`test_make_orders.py`, `test_get_orders_list.py`

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание allure-отчета о результатах тестирования**

>  `$ pytest tests/* --alluredir=allure_results`

**Просмотр allure-отчета в браузере**

>  `$ allure serve allure_results`