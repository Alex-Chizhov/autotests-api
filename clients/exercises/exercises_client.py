from clients.api_client import APIClient
from httpx import Response
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.exercises.exercises_schema import (
    GetExercisesQuerySchema,
    CreateExercisesRequestSchema,
    UpdateExercisesRequestSchema,
    GetExerciseResponseSchema,
    GetExercisesResponseSchema,
    CreateExerciseResponseSchema,
    UpdateExerciseResponseSchema
)


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
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

    def create_exercise_api(self, request: CreateExercisesRequestSchema) -> Response:
        """
        Создание задания.

        :param request: Словарь с параметрами задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/exercises', json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestSchema) -> Response:
        """
        Обновления данных задания.

        :param exercise_id: id задания.
        :param request: Словарь с параметрами задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаление задания.

        :param exercise_id: id задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Получение задания в формате json.

        :param exercise_id: id задания.
        :return: Ответ от сервера в в виде объекта GetExerciseResponseDict.
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, request: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Получение заданий в формате json.

        :param request: Словарь GetExercisesQueryDict.
        :return: Ответ от сервера в виде объекта GetExercisesResponseDict.
        """
        response = self.get_exercises_api(query=request)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExercisesRequestSchema) -> CreateExerciseResponseSchema:
        """
        Создания задания.

        :param request: Словарь формата CreateExerciseRequestDict.
        :return: Ответ от сервера в виде объекта CreateExerciseResponseDict.
        """
        response = self.create_exercise_api(request=request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Обновление задания.

        :param exercise_id: id задания.
        :param request: Словарь формата UpdateExerciseRequestDict.
        :return: Ответ от сервера в виде объекта UpdateExerciseResponseDict.
        """
        response = self.update_exercise_api(exercise_id=exercise_id, query=request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
