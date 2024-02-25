#Real-Time Chat Application with Pickling:

#Develop a simple real-time chat application where multiple clients can communicate with each other via a central server using sockets. 
#Messages sent by clients should be pickled before transmission. The server should receive pickled messages, unpickle them, and broadcast them to all connected clients.


#Requirements:
#Implement separate threads for handling client connections and message broadcasting on the server side.
#Ensure proper synchronization to handle concurrent access to shared resources (e.g., the list of connected clients).
#Allow clients to join and leave the chat room dynamically while maintaining active connections with other clients.
#Use pickling to serialize and deserialize messages exchanged between clients and the server.
import socket
import pickle

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 8080)
    client_socket.connect(server_address)

    try:
        while True:
            message = input("Enter message: ")
            # Pickle the message before sending
            pickled_message = pickle.dumps(message)
            client_socket.sendall(pickled_message)

            data = client_socket.recv(1024)
            if data:
                # Unpickle the received message
                unpickled_message = pickle.loads(data)
                print("Received:", unpickled_message)
    except KeyboardInterrupt:
        print("Client disconnected.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    run_client()
