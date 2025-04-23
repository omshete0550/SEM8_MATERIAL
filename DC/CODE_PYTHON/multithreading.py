import time
import threading

lock = threading.Lock()
ctr = 0

def inc(name):
    global ctr
    for _ in range(5):
        time.sleep(0.5)
        with lock:
            ctr = ctr + 1
            print(f"[{name}] : {ctr}")

def monitor(name):
    time.sleep(0.75)
    print(f"[{name}] : {ctr}")

t1 = threading.Thread(target=inc, args=('Thread-1', ))
t2 = threading.Thread(target=inc, args=('Thread-2', ))
threading.Thread(target=monitor, args=('Moni', ), daemon=True).start()

t1.start()
t2.start()

t1.join()
t2.join()