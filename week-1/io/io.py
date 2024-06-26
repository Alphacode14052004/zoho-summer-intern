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
