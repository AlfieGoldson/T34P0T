import socket

print("Interrogation du DNS: " + socket.gethostbyname("www.univ-tln.fr"))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("www.univ-tln.fr", 80))

request = "GET / HTTP/1.1\n"
request += "Host: www.univ-tln.fr\n"
request += "Connection: Close\n\n"

s.send(request.encode('UTF-8'))

data = s.recv(15)
print(data)

print(data.decode('utf-8'))

s.close()
