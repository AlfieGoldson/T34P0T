import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("ftp.univ-tln.fr", 21))

etat = 0

for line in s.makefile('r', encoding="UTF-8"):
    if ((etat == 0) and line.startswith("220")):
        print("send user")
        s.send("USER anonymous\n".encode('UTF-8'))
        etat = 1
    elif ((etat == 1) and line.startswith("331 ")):
        print("send password")
        s.send("PASS anonymous\n".encode('UTF-8'))
        etat = 2
    elif ((etat == 2) and line.startswith("230 Guest login ok")):
        print("send SYST command".encode('UTF-8'))
        s.send("SYST\n".encode('UTF-8'))
        etat = 3
    elif (etat == 3):
        print(line)
        s.send("QUIT\n".encode('UTF-8'))
        etat = 4
    elif (etat == 4):
        print(line)
s.close()
