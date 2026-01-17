from typing import TypedDict
from clients.api_client import APIClient
from httpx import Response


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str


class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    courseId: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Получение списка заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get('/api/v1/exercises', query=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение задания по id.

        :param exercise_id: id задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Создание задания.

        :param request: Словарь с параметрами задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str, request: CreateExercisesRequestDict) -> Response:
        """
        Обновления данных задания.

        :param exercise_id: id задания.
        :param request: Словарь с параметрами задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаление задания.

        :param exercise_id: id задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')
