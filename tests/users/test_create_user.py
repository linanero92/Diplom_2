from methods.user_methods import UserMethods
import messages
import allure


class TestCreateUser:

    @allure.title('Проверка регистрации нового пользователя')
    def test_user_create_successful(self):
        user_methods = UserMethods()
        status_code, _, _ = user_methods.create_new_user()
        assert status_code == 200

    @allure.title('Проверка регистрации нового пользователя c уже существующими данными')
    def test_create_user_with_existing_data(self):
        user_methods = UserMethods()
        status_code, response_message = user_methods.create_user_with_existing_data()
        assert status_code == 403
        assert response_message == messages.USER_EXISTS

    @allure.title('Проверка регистрации нового пользователя без ввода пароля')
    def test_create_new_user_without_password(self):
        user_methods = UserMethods()
        status_code, response_message = user_methods.create_new_user_without_password()
        assert status_code == 403
        assert response_message == messages.NOT_ENOUGH_DATA
