import socket

res = '{"status": 418, "message": "I\'m a teapot!"}'


def listen(server_socket):
    server_socket.listen(1)
    conn, addr = server_socket.accept()
    print('Connected by', addr)
    while 1:
        conn.sendall(res)
        conn.close
    listen(server_socket)


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

listen(s)
