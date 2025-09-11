import grpc
from concurrent import futures
import course_service_pb2
import course_service_pb2_grpc


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    # Обработчик запроса
    def GetCourse(self, request, context):
        return course_service_pb2.GetCourseResponse(
            course_id=request.course_id,
            title="Автотесты API",
            description="Будем изучать написание API автотестов"
        )


def serve():
    # Создаем сервер gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Регистрируем обработчик сервиса
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(
        CourseServiceServicer(), server
    )
    # Настраиваем прослушивание порта
    server.add_insecure_port('[::]:50051')
    # Запускаем сервер
    server.start()
    # Ожидаем завершения работы сервера
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
