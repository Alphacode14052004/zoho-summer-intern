import threading
import time

def io_bound_task():
    print(f"Starting I/O bound task in thread: {threading.current_thread().name}")
    time.sleep(2)  # Simulate I/O delay
    print(f"Finished I/O bound task in thread: {threading.current_thread().name}")

if __name__ == "__main__":
    threads = []
    for _ in range(5):
        t = threading.Thread(target=io_bound_task)
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
from multiprocessing import Process
import math

def cpu_bound_task(n):
    print(f"Starting CPU bound task in process: {os.getpid()}")
    result = sum(math.factorial(i) for i in range(n))
    print(f"Finished CPU bound task in process: {os.getpid()}, Result: {result}")

if __name__ == "__main__":
    processes = []
    for _ in range(5):
        p = Process(target=cpu_bound_task, args=(50000,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
