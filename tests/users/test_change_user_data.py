from methods.user_methods import UserMethods
import messages
import allure


class TestChangeUserData:

    @allure.title('Проверка изменения данных под авторизованным пользователем')
    def test_change_user_data_with_login(self):
        user_methods = UserMethods()
        status_code, response_context = user_methods.change_user_data_authorized()
        assert status_code == 200
        assert response_context is not None

    @allure.title('Проверка изменения данных пользователя без авторизации')
    def test_change_user_data_unauthorized(self):
        user_methods = UserMethods()
        status_code, response_message = user_methods.change_user_data_unauthorized()
        assert status_code == 401
        assert response_message == messages.SHOULD_BE_AUTHORIZED
