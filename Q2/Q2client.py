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

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 8080)
    client_socket.connect(server_address)

    try:
        # Define the task (simple addition)
        task = [1, 2, 3, 4, 5]

        # Pickle the task
        serialized_task = pickle.dumps(task)

        # Send the pickled task to the server
        client_socket.sendall(serialized_task)

        # Receive the result from the server
        serialized_result = client_socket.recv(1024)
        result = pickle.loads(serialized_result)
        print("Received result:", result)

    finally:
        client_socket.close()

if __name__ == "__main__":
    run_client()
