import threading
import time

file_name = "h.txt"
lock = threading.Lock()

def read_data():
    while True:
        with lock:
            with open(file_name, "r") as fle:
                data = fle.read()
                print(data)
        time.sleep(10)  

def write_data():
    while True:
        new_data = input("Enter data to write to file (type 'exit' to quit): ")
        if new_data.lower() == "exit":
            break
        with lock:
            with open(file_name, "a") as fle:
                fle.write(new_data + "\n")
                print("Data written to file:", new_data)
        time.sleep(3)  

read_thread = threading.Thread(target=read_data)
write_thread = threading.Thread(target=write_data)

read_thread.start()

while True:
    write_thread.start()
    time.sleep(10)  
    write_thread.join() 
    read_thread.join()

print("Program terminated.")
