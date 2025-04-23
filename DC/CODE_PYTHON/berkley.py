import time

def time_input(propmt):
    time = input(propmt)
    h, m = map(int, time.split(":"))
    return (h * 60 + m)

def min_to_stamp(min):
    return f"{min // 60:02d} : {min % 60:02d}"

def berkley():
    n = int(input("Enter the number of nodes: "))
    main = time_input("Enter the Main Clock Time (HH:MM): ")

    nodes = []
    for i in range(n):
        node_time = time_input(f"Enter the time for {i} node: ")
        nodes.append(node_time)

    print("\nBefore Sync:")
    for i in range(0, n):
        print(f"Clock {i} : {min_to_stamp(nodes[i])}")

    print("\nTime difference from Main: ")
    diff = []
    for i in range(0, n):
        dif = nodes[i] - main
        diff.append(dif)

    print("\nDifference in times are: ")
    for i in range(0, n):
        print(f"Clock {i} : {diff[i]}")

    offset = sum(diff) // (n + 1)
    print(f"\nAverage Offset: {offset:+} min")

    print("\nNew synchronized times:")
    print(f"Main Clock: {min_to_stamp(main + offset)}")

    for i in range(n):
        new_time = nodes[i] + (offset - diff[i])
        print(f" Clock{i}: {min_to_stamp(new_time)}")

berkley()