#Implement a client-server file transfer application where the client sends a file to the server using sockets. 
#Before transmitting the file, pickle the file object on the client side. On the server side, receive the pickled file object, unpickle it, and save it to disk.


#Requirements:
#The client should provide the file path of the file to be transferred.
#The server should specify the directory where the received file will be saved.
#Ensure error handling for file I/O operations, socket connections, and pickling/unpickling.

import socket
import pickle

def send_file(file_path, server_host, server_port):
    try:
        # Read file
        with open(file_path, 'rb') as f:
            file_data = f.read()

        # Prepare file object
        file_object = {'filename': file_path, 'data': file_data}

        # Pickle file object
        pickled_file = pickle.dumps(file_object)

        # Connect to server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_host, server_port))

        # Send pickled file
        client_socket.sendall(pickled_file)
        print("File sent successfully.")

    finally:
        client_socket.close()

def run_client():
    file_path = 'sample.txt'
    server_host = "localhost"
    server_port = 8080

    send_file(file_path, server_host, server_port)

if __name__ == "__main__":
    run_client()
