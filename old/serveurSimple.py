import socket
import sys

HOST = '127.0.0.1'
PORT = 2003

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()

while 1:
    print("serveur simple en attente...")
    mySocket.listen(5)

    connexion, adresse = mySocket.accept()
    print("Un client est connecté depuis l'adresse IP %s et le port %s" %
          (adresse[0], adresse[1]))

    connexion.send(("Vous êtes connecté au serveur "+HOST +
                    ":"+str(PORT)+".\n").encode('UTF-8'))

    while 1:
        connexion.send("Votre message ?\n".encode('UTF-8'))
        msgClient = connexion.recv(1024)
        msgClient = msgClient.decode("utf-8")

        if msgClient.upper().strip() == "FIN" or msgClient.strip() == "":
            break

        print("reçu du client>"+msgClient+"<")
        connexion.send(("ECHO : "+msgClient).encode('UTF-8'))

    connexion.send("Good Bye.".encode('UTF-8'))
    print("Connexion interrompue.")
    connexion.close()

    ch = input("Attendre un autre client ? <R>ecommencer <T>erminer ? ")
    if ch.upper() == 'T':
        break
