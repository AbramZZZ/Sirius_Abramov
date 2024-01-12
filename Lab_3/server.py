import socket
import os


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)

print("Waiting on 8080")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")
    question = client_socket.recv(1024).decode('utf-8')
    filename = question.split(' ')[1][1:]

    try:
        with open(filename, 'rb') as file:
            text = file.read()
            answer = text
    except FileNotFoundError:
        answer = b"404 Not Found"

    client_socket.sendall(answer)
    client_socket.close()

