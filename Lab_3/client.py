import socket
import sys


if len(sys.argv) != 4:
    print("Usage: client.py server_host server_port filename")
    sys.exit(1)

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))

question = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
client_socket.sendall(question.encode('utf-8'))

answer = client_socket.recv(4096)
print(answer.decode('utf-8'))

client_socket.close()
