from datetime import datetime
import socket 
from threading import Thread, Lock
from queue import Queue



N_THREADS = 500
queue = Queue()
print_lock = Lock()

def portscannig(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect((host, port))
    except:
        with print_lock:
            print(f"{host:15}: {port:5} is closed ", end='\r')
    else:
        with print_lock:
            print(f"{host:15}: {port:5} is open  ")
    finally:
        s.close()
def thread_scanning():
    global queue
    while True:
        port_number = queue.get()
        portscannig(port_number) 
        queue.task_done()
def main(host, ports):
    global queue
    for thread in range(N_THREADS):
        thread = Thread(target=thread_scanning)
        thread.daemon = True
        thread.start()
    for port in ports:
        queue.put(port)
    queue.join()
if __name__ == "__main__":
  
  print("Scanning started at:" + str(datetime.now()))
  target = input('Define a target?: ')
  host = socket.gethostbyname(target)
  ports = [ p for p in range(1, 2000)]
  main(host, ports)
