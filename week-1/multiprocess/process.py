import threading
import time

file_name = "h.txt"
lock = threading.Lock()
data = ''
# def read_data():
#     while True:
#         with lock:
#             with open(file_name, "r") as fle:
#                 data = fle.read()
#                 print(data)
#         time.sleep(10)  
lock = threading.Lock()
def write_data():
    # new_data = input("Enter data to write to file (type 'exit' to quit): ")
    new_data = 'Hello my name is venkat'
    with lock:    
        with open(file_name, "a") as fle:
            fle.write(new_data + "\n")
            print("Data written to file:", new_data)
        time.sleep(3)  

# read_thread = threading.Thread(target=read_data)
# write_thread1 = threading.Thread(target=write_data)
lst = []

for i in range(10000):
    wr_th1 = threading.Thread(target=write_data)
    wr_th1.start()
    wr_th1.join()



# read_thread.start()

# while True:
#     write_thread1.start()
#     time.sleep(10)  
#     write_thread1.join() 
    # read_thread.join()

# print("Program terminated.")
