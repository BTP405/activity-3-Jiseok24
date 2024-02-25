#Implement a client-server file transfer application where the client sends a file to the server using sockets. 
#Before transmitting the file, pickle the file object on the client side. On the server side, receive the pickled file object, unpickle it, and save it to disk.


#Requirements:
#The client should provide the file path of the file to be transferred.
#The server should specify the directory where the received file will be saved.
#Ensure error handling for file I/O operations, socket connections, and pickling/unpickling.

import socket
import pickle
import os

def receive_file(server_socket, save_directory):

    client_socket, address = server_socket.accept()
    print(f"Connection from {address}")

    # Receive pickled file object
    file_data = client_socket.recv(1024)
    file_object = pickle.loads(file_data)

    # Extract filename
    filename = os.path.basename(file_object['filename'])

    # Save file to specified directory
    save_path = os.path.join(save_directory, filename)
    with open(save_path, 'wb') as f:
        f.write(file_object['data'])
    print(f"File received and saved as {save_path}")

    client_socket.close()


def run_server():
    host = 'localhost'
    port = 8080
    save_directory = 'received_files'

    try:
        os.makedirs(save_directory, exist_ok=True)

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)

        print(f"Server is listening for incoming connections on {host}:{port}...")

        receive_file(server_socket, save_directory)
    finally:
        server_socket.close()

if __name__ == "__main__":
    run_server()
