import json
import socket
import time
import sys
import random
import numpy as np

def request_creation(job_id):
	num_map=random.randrange(1,5)
	num_reduce=random.randrange(1,3)
	job_req={"job_id":job_id,"map_tasks":[],"reduce_tasks":[]}
	for i in range(0,num_map):
		map_task={"task_id":job_id+"_M"+str(i),"duration":random.randrange(1,5)}
		job_req["map_tasks"].append(map_task)
	for i in range(0,num_reduce):
		reduce_task={"task_id":job_id+"_R"+str(i),"duration":random.randrange(1,5)}
		job_req["reduce_tasks"].append(reduce_task)
	return job_req

def req_send(job_req):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect(("localhost", 6000))
		message=json.dumps(job_req)
		s.send(message.encode())

if __name__ == '__main__':
	if(len(sys.argv)!=2):
		print("usage file_name.py number_of_requests")
		exit()
	number_of_requests=int(sys.argv[1])
	arrivals = np.random.exponential(1, size=number_of_requests-1)
	num_request=0
	current_time=last_request_time=time.time()
	job_req=request_creation(str(num_request))
	print("interval: ",0,"\n Job request :",job_req)
	req_send(job_req)
	num_request+=1
	while num_request<number_of_requests:
		interval=arrivals[num_request-1]
		while True:
			if(time.time()-last_request_time>=interval):
				break
			time.sleep(0.01)
		job_req=request_creation(str(num_request))
		print("interval: ",interval,"\n Job request :",job_req)
		req_send(job_req)
		last_request_time=time.time()
		num_request+=1
