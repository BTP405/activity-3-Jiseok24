import socket

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8080)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print("Server is listening for incoming connections...")

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()

        try:
            print("Connected to:", client_address)

            # Receive data from server
            data = client_socket.recv(1024)
            print("Received:", data.decode())

            # Send an acknowledge back to the client
            message = "Message received by the server!"
            client_socket.sendall(message.encode())

        finally:
            # Clean up the connection
            client_socket.close()

if __name__ == "__main__":
    run_server()