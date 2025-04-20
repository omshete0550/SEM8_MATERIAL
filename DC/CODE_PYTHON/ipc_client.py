import socket

HOST = "127.0.0.1"
PORT = 4568

def sendable_data(data):
    return str(data).encode("utf-8")

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Connected to server…")
        print("Commands:")
        print("  hello             - Greeting")
        print("  add <a> <b>       - Add two numbers")
        print("  square <a>        - Square a number")
        print("  exit              - Disconnect")
        
        while True:
            msg = input("Enter msg for server: ")
            s.sendall(sendable_data(msg))

            response = s.recv(1024).decode("utf-8")
            print(f"Process 1: {response}")

            if msg.lower() == "exit":
                break
