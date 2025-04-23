allocated = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
max_need = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [4, 2, 2], [5, 3, 3]]
total_resources = [10, 5, 7]
num_processes = 5
safe_seq = []

need = [[max_need[i][j] - allocated[i][j] for j in range(len(max_need[0]))] for i in range(num_processes)]
print("Need Matrix: ")
print(need)

allocated_sum = [sum(allocated[i][j] for i in range(num_processes)) for j in range(len(total_resources)) ]
available = [ total_resources[j] - allocated_sum[j] for j in range(len(total_resources))]
print("\nInitial Available Resources: ", available)

finish = [False] * num_processes
work = available.copy()
print("Work: ", work)

while True:
    found = False
    for i in range(num_processes):
        if not finish[i] and all(need[i][j] <= work[j] for j in range(len(available))):
            work = [work[j] + allocated[i][j] for j in range(len(available))]
            print(work)
            finish[i] = True
            safe_seq.append(i)
            found= True
            break
    
    if not found:
        break

print("All processes finished: ", all(finish))
print("Safe sequence: ", safe_seq if all(finish) else "No safe seq found")