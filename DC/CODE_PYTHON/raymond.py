tokens = { 1: True, 2: False, 3: False, 4: False, 5: False}
request = { 1: False, 2: False, 3: False, 4: False, 5: False}
parents = { 1: [], 2: [1], 3: [1], 4:[3], 5:[3]}
personal_queue = { 1: [], 2: [], 3: [], 4:[], 5:[]}
qu_id = []
cnt = 0

def request_cs(id):
    request[id] = True
    qu_id.append(id)
    print("queue by each process", personal_queue)
    print("req sent", request)
    print("flow", qu_id)
    parent_id = parents[id]
    if tokens[parent_id[0]] == False:
        request_cs(parent_id[0])
    else:
        final_cs(parent_id[0])

def final_cs(id):
    global cnt
    if cnt == 0:
        qu_id.append(id)
        print(qu_id)
        qu_id.reverse()
        print(qu_id)
        for i in range(len(qu_id)):
            personal_queue[qu_id[i]] = qu_id[i-len(qu_id):]
        print(personal_queue)
        request[id] = True

    cnt = cnt +1
    list_p = personal_queue[id]
    list_p = list_p[1:]
    new_entry_token = list_p[0]

    personal_queue[id] = list_p
    tokens[id] = False
    tokens[new_entry_token] = True
    print("token location", tokens)
    print("currentlt process ", new_entry_token)

    if len(personal_queue[new_entry_token]) != 1:
        final_cs(new_entry_token)
        
print("first at 4")
request_cs(4) 