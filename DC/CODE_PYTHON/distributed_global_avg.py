def to_min(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)

def calculate_skew(curr, agreed):
    return curr - agreed

def sync_clock(avg, curr):
    abs_avg = abs(avg)
    if avg > 0:
        return curr - abs_avg, "Decrease"
    elif avg < 0:
        return curr + abs_avg, "Increase"
    else:
        return curr, "No Change"

agreed_time = to_min(input("Enter the agreed upon time (HH:MM): "))
n = int(input("Enter the number of machines: "))
time_list = input("Enter current time of {n} machines (HH:MM): " ).split()

curr_time = {}
for i in range(n):
    curr_time[i+1] = to_min(time_list[i])

print("\nAgreed Upon Time (in min): ", agreed_time)

initial_skew = []
for i in range(1, n+1):
    skew = calculate_skew(curr_time[i], agreed_time)
    initial_skew.append(skew)
    print(f"Machine {i}: Initial Time = {curr_time[i]} minutes, Skew = {skew} minutes")

for i in range(1, n+1):
    curr_time[i] += 5

final_skew = []
for i in range(1, n+1):
    skew = calculate_skew(curr_time[i], agreed_time)
    final_skew.append(skew)
    print(f"Machine {i}: Final Time After 5 minutes = {curr_time[i]} minutes, Skew = {skew} minutes")

for i in range(1, n+1):
    avg_skew = (initial_skew[i-1] + final_skew[i-1]) / 2
    print(f"Machine {i}: Average Skew = {avg_skew} minutes")

    new_time, action = sync_clock(avg_skew, curr_time[i])
    print(f"Machine {i}: Current Time = {curr_time[i]} minutes, After Sync: {new_time} minutes, Action: {action}")