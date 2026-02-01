from typing import TypedDict
from clients.api_client import APIClient
from httpx import Response
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


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


class Exercise(TypedDict):
    """
    Описание структуры задания.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на создание задания.
    """
    exercise: Exercise


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на обновление задания.
    """
    exercise: Exercise


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на получение задания.
    """
    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на получение заданий.
    """
    exercises: list[Exercise]


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

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
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

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Получение задания в формате json.

        :param exercise_id: id задания.
        :return: Ответ от сервера в в виде объекта GetExerciseResponseDict.
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return response.json()

    def get_exercises(self, request: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Получение заданий в формате json.

        :param request: Словарь GetExercisesQueryDict.
        :return: Ответ от сервера в виде объекта GetExercisesResponseDict.
        """
        response = self.get_exercises_api(query=request)
        return response.json()

    def create_exercise(self, request: CreateExercisesRequestDict) -> CreateExerciseResponseDict:
        """
        Создания задания.

        :param request: Словарь формата CreateExerciseRequestDict.
        :return: Ответ от сервера в виде объекта CreateExerciseResponseDict.
        """
        response = self.create_exercise_api(request=request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestDict) -> UpdateExerciseResponseDict:
        """
        Обновление задания.

        :param exercise_id: id задания.
        :param request: Словарь формата UpdateExerciseRequestDict.
        :return: Ответ от сервера в виде объекта UpdateExerciseResponseDict.
        """
        response = self.update_exercise_api(exercise_id=exercise_id, query=request)
        return response.json()


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
