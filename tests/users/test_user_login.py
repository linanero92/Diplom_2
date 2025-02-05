from methods.user_methods import UserMethods
import messages
import allure


class TestUserLogin:

    @allure.title('Проверка авторизации под существующим пользователем')
    def test_user_login(self):
        user_methods = UserMethods()
        status_code, response_message = user_methods.user_login()
        assert status_code == 200

    @allure.title('Проверка авторизации с неверным вводом email')
    def test_user_login_with_wrong_email(self):
        user_methods = UserMethods()
        status_code, response_message = user_methods.user_login_with_wrong_email()
        assert status_code == 401
        assert response_message == messages.INCORRECT_AUTH_DATA

    @allure.title('Проверка авторизации с неверным вводом пароля')
    def test_user_login_with_wrong_password(self):
        user_methods = UserMethods()
        status_code, response_message = user_methods.user_login_with_wrong_password()
        assert status_code == 401
        assert response_message == messages.INCORRECT_AUTH_DATA
