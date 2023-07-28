from socket import *
import sys
from datetime import datetime
import time
import json
import threading
updatesPort = 6025
HeartbeatPort = 5029
masterIP = '127.0.0.1'
masterPort = 0

def execTask(num_slots,execution_pool,worker,lock):
    while 1:
        time.sleep(1)
        if execution_pool != []:
            lock.acquire()
            for task in execution_pool:
                task['duration'] -= 1
                if task['duration'] == 0:
                    sendUpdate(task,worker)
                    execution_pool.remove(task)
                    print("Number of tasks present",len(execution_pool))
                    num_slots += 1
            lock.release()

def sendUpdate(task,worker):
    print(task)
    update = {"worker_id":worker,"task_id":task['task_id']}
    print(f"Task {task['task_id']} Completed, Sending update")
    try:
        masterSocket = socket(AF_INET, SOCK_STREAM)
        masterSocket.connect((masterIP, updatesPort))
        masterSocket.send(json.dumps(update).encode())
        timing = datetime.now()
        info = "Task "+task['task_id']+" Completed at " + str(timing)
        print(info)
    except TimeoutError:
        print("server busy, sleeping and trying again...")
        time.sleep(1)
        sendUpdate(task,worker)
    except ConnectionError:
        time.sleep(1)
        sendUpdate(task,worker)

def heartbeat_send(num_slots,execution_pool,worker,lock):
    print("Initialising heartbeats")
    while 1:
        masterSocket = socket(AF_INET, SOCK_STREAM)
        try:
            masterSocket.connect((masterIP, HeartbeatPort))
            print("Sending HeartBeat...",datetime.now())
            lock.acquire()
            update = {"worker_id":worker,"num_slots":num_slots}
            lock.release()
            masterSocket.send(json.dumps(update).encode())
            acknowledgeWorker = masterSocket.recv(1024)
            masterSocket.close()
        except ConnectionRefusedError:
            print("Connection refused,trying again in 1s...")
        except TimeoutError:
            print('Timeout, retrying in 1s... ')
        time.sleep(0.5)

def receive_task(num_slots,execution_pool,worker,lock):
    global masterPort
    masterSocket = socket(AF_INET, SOCK_STREAM)
    masterSocket.bind((masterIP, masterPort))
    masterSocket.listen(1)
    print("Listening for events...")
    while 1:
        masterConnection, _ = masterSocket.accept()
        task = masterConnection.recv(1024)
        task_to_do = json.loads(task.decode())
        timing = datetime.now()
        info = "Received Task " +str(task_to_do['task_id'])+" at "+str(timing)+" Running..."
        print(info)
        lock.acquire()
        execution_pool.append(task_to_do)
        num_slots-=1
        lock.release()
        print("Number of tasks present",len(execution_pool))
        masterConnection.close()

def main():
    if len(sys.argv) != 4:
        print('usage file_name.py port worker_id num_slots')
        exit()
    global masterPort
    execution_pool = list()  
    lock = threading.Lock()
    num_slots = int(sys.argv[3])
    worker = sys.argv[2]
    masterPort = int(sys.argv[1])
    t1 = threading.Thread(target=receive_task,args=(num_slots,execution_pool,worker,lock))
    t2 = threading.Thread(target=heartbeat_send,args=(num_slots,execution_pool,worker,lock))
    t3 = threading.Thread(target=execTask,args=(num_slots,execution_pool,worker,lock))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
main()
