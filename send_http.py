import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 7799))
print("客户端正在连接127.0.0.1:7799")
sock.listen(100)
cli_sock,address = sock.accept()
print(cli_sock)
print("客户端进行了连接")

sock.close()
