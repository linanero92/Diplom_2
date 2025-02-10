from methods.user_methods import UserMethods
import messages
import allure


class TestUserLogin:

    @allure.title('Проверка авторизации под существующим пользователем')
    def test_user_login(self, create_user_and_delete):
        email, password, name, _, _ = create_user_and_delete
        user_methods = UserMethods()
        status_code, response_message = user_methods.user_login(email, password, name)
        assert status_code == 200

    @allure.title('Проверка авторизации с неверным вводом email')
    def test_user_login_with_wrong_email(self, create_user_and_delete):
        _, password, name, _, _ =create_user_and_delete
        user_methods = UserMethods()
        status_code, response_message = user_methods.user_login_with_wrong_email(password, name)
        assert status_code == 401
        assert response_message == messages.INCORRECT_AUTH_DATA

    @allure.title('Проверка авторизации с неверным вводом пароля')
    def test_user_login_with_wrong_password(self, create_user_and_delete):
        email, _, name, _, _ = create_user_and_delete
        user_methods = UserMethods()
        status_code, response_message = user_methods.user_login_with_wrong_password(email, name)
        assert status_code == 401
        assert response_message == messages.INCORRECT_AUTH_DATA
