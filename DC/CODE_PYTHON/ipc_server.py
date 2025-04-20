import socket

HOST = '127.0.0.1'
PORT = 4568

def sendable_data(data):
    return str(data).encode('utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Server is running.....")
    s.listen()

    conn, addr = s.accept()

    with conn:
        print("Client is connected...")
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break

            print(f"Received from client: {data}")

            if data.lower() == 'exit':
                conn.sendall(sendable_data("Connection is closed! Bye."))
                break
            elif data.lower() == 'hello':
                response = "Server: Hello Good Morning"
            elif data.lower().startswith("add "):
                try:
                    parts = data.split()
                    a = int(parts[1])
                    b = int(parts[2])
                    result = a+b
                    response = f"Addition of {a} and {b} is {result}"
                except:
                    response = "Error: Please provide two numbers. Format: add 5 10"
            elif data.lower().startswith("square "):
                try:
                    parts = data.split()
                    a = int(parts[1])
                    result = a * a
                    response = f"Square of {a} is {result}"
                except:
                    response = "Error: Please provide one number. Format: square 6"
            else:
                response = f"Server received: {data}"

            conn.sendall(sendable_data(response))