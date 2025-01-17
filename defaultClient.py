import socket

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 8080)
    client_socket.connect(server_address)

    try:
        message = "Hello server!"
        client_socket.sendall(message.encode())

        data = client_socket.recv(1024)
        print("Received acknowledgment:", data.decode())
    finally:
        client_socket.close()

if __name__ == "__main__":
    run_client()