from methods.order_methods import OrderMethods
import messages
import allure


class TestMakeOrder:

    @allure.title('Проверка создания заказа под авторизованным пользователем')
    def test_make_order_authorized(self):
        order_methods = OrderMethods()
        status_code = order_methods.make_order_authorized()
        assert status_code == 200

    @allure.title('Проверка создания заказа без авторизации пользователя')
    def test_make_order_unauthorized(self):
        order_methods = OrderMethods()
        status_code = order_methods.make_order_unauthorized()
        assert status_code == 200

    @allure.title('Проверка создания заказа без добавления ингредиентов под авторизованным пользователем')
    def test_make_order_without_ingredients_authorized(self):
        order_methods = OrderMethods()
        status_code, response_message = order_methods.make_order_without_ingredients_authorized()
        assert status_code == 400
        assert response_message == messages.NO_INGREDIENTS

    @allure.title('Проверка создания заказа с невалидными ингредиентами без авторизации пользователя')
    def test_make_order_with_wrong_ingredients_unauthorized(self):
        order_methods = OrderMethods()
        status_code = order_methods.make_order_with_wrong_ingredients_unauthorized()
        assert status_code == 500
