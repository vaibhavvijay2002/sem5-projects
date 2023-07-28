import threading
import sys
from socket import *
import random
from datetime import datetime
import time
import json
from queue import Queue
HeartbeatPort = 5029
workerIP = '127.0.0.1'
curr_worker_index = 0
requestPort = 6000
updatesPort = 6025

def listenUpdates(task_execution_pool, worker_slots, algo, lock):
    masterSocket = socket(AF_INET, SOCK_STREAM)
    masterSocket.bind((workerIP, updatesPort))
    masterSocket.listen(1)
    print("listening for updates...")
    while 1:
        workerHeartBeat, _ = masterSocket.accept()
        worker_update = workerHeartBeat.recv(2048)
        taskCompl = json.loads(worker_update.decode())
        job_id = taskCompl['task_id'].split("_")[0]
        task_type = taskCompl['task_id'].split("_")[1][0]
        worker = taskCompl['worker_id']
        time_of_update = datetime.now().time()
        lock.acquire()
        for i in range(len(task_execution_pool)):
            if job_id in task_execution_pool[i].keys():
                if task_type == "M":
                    task_execution_pool[i][job_id]['num_map'] -= 1
                    worker_slots[int(worker)]['slots'] += 1
                    print(f"increasing worker : {worker}")
                    show_slots(worker_slots)
                if task_type == "R":
                    task_execution_pool[i][job_id]['num_reduce'] -= 1
                    worker_slots[int(worker)]['slots'] += 1
                    print(f"increasing worker : {worker}")
                    show_slots(worker_slots)
                if task_execution_pool[i][job_id]['num_map'] == 0 and task_execution_pool[i][job_id]['num_reduce'] == 0:
                    time_of_update = datetime.now().time()
                    info = 'Completed Job '+job_id+' at '+str(time_of_update)+" "+algo
                    print(info)
        lock.release()
        info = 'Received task '+taskCompl['task_id']+' at '+str(time_of_update)
        print(info)
        workerHeartBeat.close()

def determineWorker(worker_info, algo, lock):
    global curr_worker_index
    lock.acquire()
    all_workers = [i for i in worker_info.keys()]
    slots = [worker_info[i]['slots'] for i in worker_info]
    if algo == "random":
        worker_id = all_workers[random.randrange(0, len(all_workers))]
        if worker_info[worker_id]['slots'] > 0:
            lock.release()
            return worker_id
        else:
            lock.release()
            time.sleep(1)
            return determineWorker(worker_info, algo, lock)
    if algo == "ll":
        worker_id = all_workers[slots.index(max(slots))]
        if worker_info[worker_id]['slots'] > 0:
            lock.release()
            return worker_id
        else:
            lock.release()
            time.sleep(1)
            return determineWorker(worker_info, algo, lock)

def heartbeatListen():
    masterSocket = socket(AF_INET, SOCK_STREAM)
    masterSocket.bind((workerIP, HeartbeatPort))
    masterSocket.listen(1)
    print("listening for heartbeats...")
    while 1:
        workerHeartBeat, _ = masterSocket.accept()
        worker_update = workerHeartBeat.recv(2048)
        workerHeartBeat.close()

def sendingTask(worker_slots, algo, task_execution_pool, task_queue, lock):
    while 1:
        lock.acquire()
        if not task_queue.empty():
            task = task_queue.get()
            lock.release()
            workerId = determineWorker(worker_slots, algo, lock)
            lock.acquire()
            print(f'reducing worker {workerId}')
            worker_slots[workerId]['slots'] -= 1
            show_slots(worker_slots)
            lock.release()
            worker = worker_slots[workerId]
            time_of_update = datetime.now().time()
            info = 'sending task ' + str(task['task_id'])+ ' to '+ str(workerId) + ' at ' + str(time_of_update)+' algo '+algo
            print(info)
            workerSocket = socket(AF_INET, SOCK_STREAM)
            workerSocket.connect((workerIP, worker['port']))
            workerSocket.send(json.dumps(task).encode())
        else:
            lock.release()
            time.sleep(1)

def show_slots(worker_slots):
        print("-----------------------")
        for i in worker_slots:
            print("Worker: ", i, "Slots: ", worker_slots[i]['slots'])
        print("-----------------------")

def taskReceiver(algo, task_execution_pool, task_queue, jobs, lock):
    masterSocket = socket(AF_INET, SOCK_STREAM)
    masterSocket.bind((workerIP, requestPort))
    masterSocket.listen(1)
    print("listening for Tasks...")
    while 1:
        masterConnection, _ = masterSocket.accept()
        taskJson = masterConnection.recv(1024)
        masterConnection.close()
        job = json.loads(taskJson.decode())
        if job['map_tasks'] != []:
            time_of_update = datetime.now().time()
            info = 'Received Job '+job['job_id']+' at '+str(time_of_update)+" "+algo
            print(info)
            lock.acquire()
            job_info = {job['job_id']: {'num_map': len(job['map_tasks']), 'num_reduce': len(job['reduce_tasks'])}}
            task_execution_pool.append(job_info)
            jobs[job['job_id']] = job['reduce_tasks']
            for task in job['map_tasks']:
                task_queue.put(task)
            for task in job['reduce_tasks']:
                task_queue.put(task)
            lock.release()


def main():
    if len(sys.argv) != 3:
        print('The format to input is: usage file_name.py config.json scheduling_algo')
        exit()
    config = sys.argv[1]
    f = open(config, "r")
    worker_info = json.load(f)
    algo = sys.argv[2]
    workers = worker_info['workers']
    worker_slots = {i['worker_id']: {
        'slots': i['slots'], 'port': i['port']} for i in workers}
    lock = threading.Lock()
    task_execution_pool = list()
    jobs = dict()
    task_queue = Queue()
    t1 = threading.Thread(target=taskReceiver,args = (algo, task_execution_pool, task_queue, jobs, lock))
    t2 = threading.Thread(target=heartbeatListen,args = ())
    t3 = threading.Thread(target=listenUpdates,args = (task_execution_pool, worker_slots, algo, lock))
    t4 = threading.Thread(target=sendingTask,args = (worker_slots, algo, task_execution_pool, task_queue, lock))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
main()
