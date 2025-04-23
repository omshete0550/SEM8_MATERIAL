import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))

print("Server started at ", 5000)
server.listen(1)
conn, addr = server.accept()
print(f"This is the adddress {addr}")

while True:
    client_msg = conn.recv(1024).decode()
    if client_msg.lower() == 'exit':
        print("[Client] ended the chat")
        break
    print(f"[Client]: {client_msg}")

    send_msg = input('[Server]: ')
    if send_msg.lower() == 'exit':
        break
    conn.send(send_msg.encode())

conn.close()
server.close()