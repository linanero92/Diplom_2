from methods.order_methods import OrderMethods
import messages
import allure


class TestGetOrdersList:

    @allure.title('Проверка получения списка заказов под авторизованным пользователем')
    def test_get_orders_list_authorized(self, create_user_and_delete):
        email, password, _, token = create_user_and_delete
        headers = {'Authorization': str(token)}
        order_methods = OrderMethods()
        status_code, response_context = order_methods.get_orders_list_authorized(headers)

        assert status_code == 200
        assert 'orders' in response_context.keys()

    @allure.title('Проверка получения списка заказов без авторизации пользователя')
    def test_get_orders_list_unauthorized(self):
        order_methods = OrderMethods()
        status_code, response_message = order_methods.get_orders_list_unauthorized()

        assert status_code == 401
        assert response_message == messages.SHOULD_BE_AUTHORIZED
