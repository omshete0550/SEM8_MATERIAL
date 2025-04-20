import socket
import threading

clients = {}
lock = threading.Lock()

def handle_client(client_socket, client_address):
    try:
        name = client_socket.recv(1024).decode('UTF-8')
        with lock:
            clients[client_socket] = name
        print(f"New client connected: {client_address} as {name}")
        broadcast(f"{name} has joined the chat.", client_socket)

        while True:
            message = client_socket.recv(1024).decode('UTF-8')
            if message:
                print(f"{name} : {message}")
                broadcast(f"{name} : {message}", client_socket)
            else:
                break
    
    except:
        pass
    finally:
        remove_client(client_socket)


def broadcast(message, sender_socket):
    with lock:
        for client in clients:
            if client != sender_socket:
                try:
                    client.sendall(message.encode('UTF-8'))
                except:
                    remove_client(client)

def remove_client(client_socket):
    with lock:
        name = clients.get(client_socket, "Unknown")
        print(f"{name} disconnected")
        broadcast(f"{name} disconnected", client_socket)

        if client_socket in clients:
            del clients[client_socket]
        
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8888))
    server_socket.listen()
    print("Group chat server is running....")

    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

start_server()