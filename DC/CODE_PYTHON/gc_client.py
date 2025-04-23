import socket
import threading

def receive_msg(client_socket):
    while True:
        try:
            reply = client_socket.recv(1024).decode()
            if reply:
                print(f"\nReply: {reply}")
            else:
                break
        except:
            break

    print("Disconnected from server.")
    client_socket.close()

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('localhost', 8888))
        print("Connected to server...")
        name = input("Enter your name: ")
        client.send(name.encode('utf-8'))

        threading.Thread(target=receive_msg, args=(client, ), daemon=True).start()
        while True:
            msg = input("\nEnter the message: ")
            if msg:
                client.send(msg.encode('utf-8'))


    except Exception as e:
        print(f"Connection error {e}")
        client.close()

start_client()