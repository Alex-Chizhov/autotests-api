import grpc
import course_service_pb2
import course_service_pb2_grpc


def run():
    # Устанавливаем соединение с сервером
    channel = grpc.insecure_channel('localhost:50051')
    stub = course_service_pb2_grpc.CourseServiceStub(channel)
    # Формируем запрос
    request = course_service_pb2.GetCourseRequest(course_id="api-course")
    # Вызываем метод GetCourse
    response = stub.GetCourse(request)
    # Выводим ответ в консоль
    print(response)

if __name__ == '__main__':
    run()
