import socket
import sys

isTeapot = False
props = ["XD", 'lol']


def processRequest(request):
    if (isTeapot):
        res = "HTCPCP/1.0 418 I'm a teapot!"
        return res

    lines = request.split('\n')
    method = lines[0].split(" ")[0]
    body = lines[1:]

    if (method == "BREW" or method == "POST"):
        res = BREW(body)
    elif (method == "GET"):
        res = GET(body)
    elif (method == "PROPFIND"):
        res = PROPFIND(body)
    else:
        res = "HTCPCP/1.0 400 Bad Request"
    return res


def BREW(body):
    res = "HTCPCP/1.0 201 Updated\n"

    return res


def GET(body):
    res = "HTCPCP/1.0 200 OK\n\n"
    for k in props:
        res += k + "\n"
    return res


def PROPFIND(body):
    res = "HTCPCP/1.0 200 OK\n\n"
    for k in props:
        res += k + "\n"
    return res


HOST = ''
PORT = 31199

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()

while 1:
    print("Server listening...")
    mySocket.listen(5)

    connexion, adresse = mySocket.accept()
    print("Client: IP %s et le port %s" % (adresse[0], adresse[1]))

    connexion.send('Connected!'.encode('UTF-8'))

    msgClient = connexion.recv(1024)
    msgClient = msgClient.decode("utf-8")

    res = processRequest(msgClient.strip())
    connexion.send(res.encode('UTF-8'))

    connexion.close()

    # ch = input("Attendre un autre client ? <R>ecommencer <T>erminer ? ")
    # if ch.upper() == 'T':
    #     break
