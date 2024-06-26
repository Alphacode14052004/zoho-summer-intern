import os

def child():
    print(f"Child process PID: {os.getpid()}")

def parent():
    print(f"Parent process PID: {os.getpid()}")
    pid = os.fork()
    if pid == 0:
        child()
    else:
        print(f"Child process created with PID: {pid}")

if __name__ == "__main__":
    parent()
