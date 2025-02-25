import socket
import threading

server_ip, server_port = '127.0.0.1', 12345

def receive_message(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg:
                print(msg)
            else:
                break
        except Exception as e:
            print(e)
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
    receive_thread.start()

    while True:
        msg = input()
        if msg == 'quit': break
        client_socket.send(msg.encode())

    client_socket.close()


if __name__ == '__main__':
    main()  
