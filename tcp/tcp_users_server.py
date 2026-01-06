import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(10)
    print("Сервер запущен и ожидает подключения...")

    total_messages = []
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {message}")
        total_messages.append(message)
        response = '\n'.join(total_messages)
        client_socket.send(response.encode('utf-8'))
        client_socket.close()


if __name__ == "__main__":
    server()
