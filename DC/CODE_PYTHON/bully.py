num = int(input("Enter the number of processes: "))
processes = [True for _ in range(num)]

crashed_id = int(input("Enter the crashed ID: "))
processes[crashed_id] = False

initiator = int(input("Enter the process ID who initiate the election: "))
print(f"Process {crashed_id} has crashed")
print(f"Process {initiator} initiates the election")

def send_election_msg(from_id):
    print(f"Election message sent from {from_id} to higher ID processes.")
    received_okay = False
    
    for i in range(from_id+1, num):
        if processes[i]:
            print(f"Okay message from {i} to {from_id}")
            received_okay = True
            send_election_msg(i)
            break

    if not received_okay:
        declare_coordinator(from_id)

def declare_coordinator(coordinator_id):
    print(f"Final Coordinator is {coordinator_id}")
    for i in range(num):
        if i != coordinator_id and processes[i]:
            print(f"Message to {i} : Coordinator is {coordinator_id}")

send_election_msg(initiator)