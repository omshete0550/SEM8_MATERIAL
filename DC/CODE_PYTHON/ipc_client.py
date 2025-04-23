import socket

port = 5000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Client is Starting.....")
client.connect(('localhost', port))

print(f"Client started at port {port}")
print("Enter the message You want to send (exit to end the conn)")

while True:
    input_msg = input("[Client]: ")
    client.send(input_msg.encode())
    if input_msg.lower() == 'exit':
        print("[Client]: Ended the chat....")
        break

    server_msg = client.recv(1024).decode()
    if server_msg.lower() == 'exit':
        print("[Server]: Ended the chat....")
        break
    print(f"[Server]: {server_msg}")

client.close()