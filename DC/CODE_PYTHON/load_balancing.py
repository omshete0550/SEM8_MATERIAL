print("Enter the number of servers amd processors")
server, processor = input().split(',')
server = int(server)
processor = int(processor)

def adjust():
    processor_in_server = [0] * (server)
    processor_ctr = processor
    print(processor_in_server)
    i = 0

    while i != -1: 
        if processor_ctr == 0:
            break
        processor_in_server[i] += 1
        processor_ctr -= 1
        
        if i == (server - 1):
            i = -1
        i += 1
    print(processor_in_server)

adjust()

while True:
    print("1. Add Servers 2. Remove Servers 3. Add Processors 4. Remove Processors 5. Exit")
    choice = int(input())

    if choice == 1:
        print("Enter the number of extra servers: ")
        extra = int(input())
        server += extra
        adjust()

    elif choice == 2:
        print("Enter the number of servers to remove: ")
        rm = int(input())
        server -= rm
        adjust()

    elif choice == 3:
        print("Enter the number of extra processors: ")
        extra = int(input())
        processor += extra
        adjust()

    elif choice == 4:
        print("Enter the number of processors to remove: ")
        rm = int(input())
        processor -= rm
        adjust()

    elif choice == 5:
        break