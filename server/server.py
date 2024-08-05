import socket
import threading

server_ip, server_port = '127.0.0.1', 12345

def handle(client_socket, addr):
    print(f'New player joined from {addr}!')
    while True:
        try:
            data = client_socket.recv(1024).decode()
            print(data)
            client_socket.send(f'Message recieved: {data}'.encode())
        except Exception as e:
            print(e)
            break
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(2)

    print(f'Server listening on {server_ip}:{server_port}')

    while True:
        client_socket, client_addr = server_socket.accept()
        handler = threading.Thread(target=handle, args=(client_socket, client_addr))
        handler.start()

if __name__ == '__main__':
    main()
