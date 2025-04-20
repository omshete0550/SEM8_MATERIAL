import socket
import threading

def receive_message(client_socket):
    while True:
        try:
            reply = client_socket.recv(1024).decode('UTF-8')
            if reply:
                print(reply)
            else:
                break
        except:
            break
    
    print("Disconnectd from server.")
    client_socket.close()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 8888))
        print("Connected to server.")
        name = input("Enter your name: ")
        client_socket.send(name.encode('utf-8'))

        threading.Thread(target=receive_message, args=(client_socket, ), daemon=True).start()

        while True:
            message = input()
            if message:
                client_socket.send(message.encode('utf-8'))
        
    except Exception as e:
        print(f"Connection error: {e}")
        client_socket.close()

start_client()