n = int(input("Enter the number of sites: "))

request_set = {i : [j for j in range(1, n+1) if j != i] for i in range(1, n+1)}
num_requests = int(input("Enter the number of sites who wants to enter the critical section: "))

required_sites = []
for _ in range(num_requests):
    timestamp, id = map(int, input("Enter the timestamp and site ID: ").split())
    required_sites.append((timestamp, id))
required_sites.sort()

print("\n-----------------Request Phase---------------------")
for timestamp, site_id in required_sites:
    for j in request_set[site_id]:
        print(f"Request sent from Site {site_id} to Site {j}")

pending_task = [site_id for _, site_id in required_sites]

print("\n-----------------Reply & CS Phase---------------------")
for timestamp, site_id in required_sites:
    for i in request_set[site_id]:
        if i not in pending_task:
            print(f"Site {i} sends reply to Site {site_id}")
        else:
            for peer_time, peer_id in required_sites:
                if peer_id == i and peer_time > timestamp:
                    print(f"Site {i} sends reply to site {site_id}")
                    break
    
    print(f"Site {site_id} enters the Critical Section")
    input("Press Enter to exit CS...")
    print(f"<<< Site {site_id} EXITS the Critical Section\n")

    pending_task.remove(site_id)