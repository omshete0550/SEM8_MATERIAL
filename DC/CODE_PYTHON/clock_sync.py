clock1 = int(input("Enter the initial time for Process 1: "))
clock2 = int(input("Enter the initial time for Process 2: "))

def send(clock):
    clock += 1
    return clock

def receive(receiver_clock, sender_clock):
    return max(receiver_clock, sender_clock) + 1

communication_queue = []

while True:
    print("\n---- Menu ----")
    print("1. Process 1 sends packet")
    print("2. Process 2 sends packet")
    print("3. Process 1 receives packet")
    print("4. Process 2 receives packet")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        clock1 = send(clock1)
        communication_queue.append(('P1', clock1))
        print(f"Process 1 sends the packet at time {clock1}")

    elif choice == '2':
        clock2 = send(clock2)
        communication_queue.append(('P2', clock2))
        print(f"Process 2 sends the packet at time {clock1}")

    elif choice == '3':
        if communication_queue:
            sender, sender_time = communication_queue.pop(0)
            clock1 = receive(clock1, sender_time)
            print(f"Process 1 receives a packet (from {sender}) at time {clock1}")
        else:
            print("No packets to receive.")
    elif choice == '4':
        if communication_queue:
            sender, sender_time = communication_queue.pop(0)
            clock2 = receive(clock2, sender_time)
            print(f"Process 2 receives a packet (from {sender}) at time {clock2}")
        else:
            print("No packets to receive.")
    elif choice == '5':
        print("Exiting simulation.")
        break
    else:
        print("Invalid input. Try again!")
    
    print(f"Current clocks -> Process 1: {clock1}, Process 2: {clock2}")