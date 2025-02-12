from methods.order_methods import OrderMethods
import messages
import allure


class TestGetOrdersList:

    @allure.title('Проверка получения списка заказов под авторизованным пользователем')
    def test_get_orders_list_authorized(self, create_user_and_delete):
        email, password, name, _, _ = create_user_and_delete
        order_methods = OrderMethods()
        status_code, response_message = order_methods.get_orders_list_authorized(email, password, name)

        assert status_code == 200
        assert 'orders' in response_message

    @allure.title('Проверка получения списка заказов без авторизации пользователя')
    def test_get_orders_list_unauthorized(self):
        order_methods = OrderMethods()
        status_code, response_message = order_methods.get_orders_list_unauthorized()

        assert status_code == 401
        assert response_message == messages.SHOULD_BE_AUTHORIZED
