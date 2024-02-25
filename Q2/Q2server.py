#Distributed Task Queue with Pickling:

#Create a distributed task queue system where tasks are sent from a client to multiple worker nodes for processing using sockets. 
#Tasks can be any Python function that can be pickled. Implement both the client and worker nodes. 
#The client sends tasks (pickled Python functions and their arguments) to available worker nodes, and each worker node executes the task and returns the result to the client.

#Requirements:
#Implement a protocol for serializing and deserializing tasks using pickling.
#Handle task distribution, execution, and result retrieval in both the client and worker nodes.
#Ensure fault tolerance and scalability by handling connection errors, timeouts, and dynamic addition/removal of worker nodes.

import socket
import pickle

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

            # Receive pickled task from client
            serialized_task = client_socket.recv(1024)
            task = pickle.loads(serialized_task)

            # Execute the task (addition)
            result = sum(task)

            print("Task result:", result)

            # Send back the result to the client
            serialized_result = pickle.dumps(result)
            client_socket.sendall(serialized_result)

        finally:
            # Clean up the connection
            client_socket.close()

if __name__ == "__main__":
    run_server()
