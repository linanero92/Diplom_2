from methods.order_methods import OrderMethods
import messages
import allure


class TestGetOrdersList:

    def test_get_orders_list_authorized(self):
        order_methods = OrderMethods()
        status_code, response_message = order_methods.get_orders_list_authorized()
        assert status_code == 200

    def test_get_orders_list_unauthorized(self):
        order_methods = OrderMethods()
        status_code, response_message = order_methods.get_orders_list_unauthorized()
        assert status_code == 401
        assert response_message == messages.SHOULD_BE_AUTHORIZED
