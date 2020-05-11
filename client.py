import socket

HOST = 'localhost'
PORT = 31199

print("Interrogation du DNS: " + socket.gethostbyname(HOST))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

request = "PROPFIND / HTCPCP/1.0\n"
request += "Host: localhost\n"
request += "Content-Type: application/coffee-pot-command\n"
request += "Accept-Additions: Cream; Vanilla; Whisky\n"

print(s.recv(1024).decode('UTF-8'))

s.send(request.encode('UTF-8'))

data = s.recv(1024).decode('UTF-8')

print(data)

s.close()
