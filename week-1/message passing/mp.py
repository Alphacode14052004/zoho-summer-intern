from multiprocessing import Process, Queue

def sender(q):
    q.put("Hello from child process")

def receiver(q):
    msg = q.get()
    print(f"Received message: {msg}")

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=sender, args=(q,))
    p2 = Process(target=receiver, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
