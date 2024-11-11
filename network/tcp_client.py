import socket
from network.config import SERVER_IP, PORT

def connect_server():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, PORT))
        print("Connected to server")
        return client_socket
    except Exception as e:
        print("Failed to connect:", e)
        return None

def send_data(client_socket, data):
    try:
        client_socket.send(data.encode())
        print("Data sent:", data)
        ack = client_socket.recv(1024)
        print("Acknowledgment received:", ack.decode())
    except Exception as e:
        print("Failed to send data:", e)