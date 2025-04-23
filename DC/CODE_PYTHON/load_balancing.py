def adjust(nodes, processes):
    processes_in_nodes = [0] * nodes
    i = 0

    for _ in range(processes):
        processes_in_nodes[i] += 1
        i = (i + 1) % nodes 

    print(f"Current Distribution Load: {processes_in_nodes}")

print("Enter the number of nodes and processes (e.g. 3, 10): ")
nodes, processes = input().split(", ")
nodes = int(nodes)
processes = int(processes)

adjust(nodes, processes)

while True:
    print("1. Add Nodes 2. Remove Nodes 3. Add Processes 4. Remove Processes 5. Exit")
    chs = int(input("Enter choice: "))

    if chs == 1:
        extra = int(input("Enter the number of extra nodes: "))
        nodes += extra
        adjust(nodes, processes)
    
    elif chs == 2:
        rm = int(input("Enter the number of nodes to remove: "))
        if rm < nodes:
            nodes -= rm
        else:
            print("Cannot remove more nodes than available.")
        adjust(nodes, processes)
    
    elif chs == 3:
        extra = int(input("Enter the number of extra processes: "))
        processes += extra
        adjust(nodes, processes)

    elif chs == 4:
        rm = int(input("Enter the number of processes to remove: "))
        if rm < processes:
            processes -= rm
        else:
            print("Cannot remove more processes than available.")
        adjust(nodes, processes)
    
    elif chs == 5:
        break

    else:
        print("Invalid choice. Try again.")