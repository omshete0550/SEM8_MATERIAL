import socket
import threading

clients = {}
lock = threading.Lock()

def handle_client(client_socket, client_addr):
    try:
        name = client_socket.recv(1024).decode('utf-8')
        with lock:
            clients[client_socket] = name
        print(f"New client is connected {client_addr} as {name}")
        broadcast(f"{name} has joined the chat", client_socket)

        while True:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg:
                print(f"{name}: {msg}")
                broadcast(f"{name}: {msg}", client_socket)
            else:
                break
    except:
        pass
    finally:
        remove_client(client_socket)

def broadcast(msg, client_socket):
    with lock:
        for client in clients:
            if client != client_socket:
                try:
                    client.sendall(msg.encode('utf-8'))
                except:
                    remove_client(client)

def remove_client(client_socket):
    with lock:
        name = clients.get(client_socket, "Unknown")
        print(f"{name} has disconnectd.")
        broadcast(f"{name} disconnected.", client_socket)

        if client_socket in clients:
            del client_socket
        
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8888))
    server.listen()

    print("Group Chat Server is Running.....")

    while True:
        client_socket, client_addr  = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_addr)).start()

start_server()