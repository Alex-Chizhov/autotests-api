from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса создания пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод создания пользователя.

        :param request: Словарь с данными для создания пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/users", json=request)