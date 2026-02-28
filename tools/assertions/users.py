from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from clients.users.users_schema import UserSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, name="email")
    assert_equal(response.user.last_name, request.last_name, name="last_name")
    assert_equal(response.user.first_name, request.first_name, name="first_name")
    assert_equal(response.user.middle_name, request.middle_name, name="middle_name")

def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет корректность данных пользователя.

    :param actual: Фактические данные пользователя.
    :param expected: Ожидаемые данные пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")

def assert_get_user_response(actual: GetUserResponseSchema, expected: CreateUserResponseSchema):
    """
    Проверяет, что данные пользователя при создании и при запросе совпадают

    :param actual: Фактические данные пользователя.
    :param expected: Ожидаемые данные пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_user(actual.user, expected.user)
