tokens = {1: True, 2: False, 3: False, 4: False, 5: False}
parents = {1: None, 2: 1, 3: 1, 4: 3, 5: 3}
queues = {i: [] for i in range(1, 6)}

def display_queue():
    print("Current Queue: ")
    for k, v in queues.items():
        print(f" - Site {k} : {v}")

def request_cs(site_id):
    if tokens[site_id]:
        print(f"Site {site_id} already has the token and can enter the CS.")
        display_queue()
        return
    
    parent = parents[site_id]
    if site_id not in queues[parent]:
        queues[parent].append(site_id)
        print(f"Site {site_id} requests token via Parent {parent}")
        display_queue()

    request_cs(parent)

def pass_token(current_holder):
    while queues[current_holder]:
        next_site = queues[current_holder].pop(0)
        tokens[current_holder] = False
        print(f"Tokens passed from Site {current_holder} -> Site {next_site} ")
        display_queue()
        current_holder = next_site

    print(f"Site {current_holder} has the token and can enter the CS")
    display_queue()
    
print("Site 4 wants to enter the Critical Section: ")
request_cs(4)

print("Passing token along the request path: ")
pass_token(1)
