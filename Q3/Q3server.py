#Real-Time Chat Application with Pickling:

#Develop a simple real-time chat application where multiple clients can communicate with each other via a central server using sockets. 
#Messages sent by clients should be pickled before transmission. The server should receive pickled messages, unpickle them, and broadcast them to all connected clients.


#Requirements:
#Implement separate threads for handling client connections and message broadcasting on the server side.
#Ensure proper synchronization to handle concurrent access to shared resources (e.g., the list of connected clients).
#Allow clients to join and leave the chat room dynamically while maintaining active connections with other clients.
#Use pickling to serialize and deserialize messages exchanged between clients and the server.
import socket
import threading
import pickle

HOST = 'localhost'
PORT = 8080

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")

    while True:
        try:
            # Receive pickled message from client
            message = client_socket.recv(1024)
            if not message:
                print(f"Connection from {client_address} closed.")
                break
            
            # Unpickle the received message
            unpickled_message = pickle.loads(message)
            
            # Broadcast the message to all clients
            broadcast(unpickled_message)
        except Exception as e:
            print(f"Error: {e}")
            break
    
    # Remove client from the list when connection is closed
    clients.remove(client_socket)
    client_socket.close()

# Function to broadcast message to all connected clients
def broadcast(message):
    for client in clients:
        try:
            # Pickle the message before sending
            pickled_message = pickle.dumps(message)
            client.send(pickled_message)
        except:
            # Remove the client if unable to send message
            clients.remove(client)

clients = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
