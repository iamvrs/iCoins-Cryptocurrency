import socket
import threading

class Node:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        server_thread = threading.Thread(target=self.start_server)
        server_thread.start()

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)

        print(f"Node listening on {self.host}:{self.port}")

        while True:
            client_socket, addr = server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        data = client_socket.recv(1024).decode()
        print(f"Received data: {data}")
        client_socket.close()

# Example usage:
node1 = Node("localhost", 5000)
node2 = Node("localhost", 5001)

node1.start()
node2.start()

# Simulate communication between nodes
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 5000))
client_socket.send("Hello from node2".encode())
client_socket.close()
