import json
worker_num = int(input("enter number of worker nodes: "))
l = []
for i in range(1,worker_num + 1):
	print("for worker with id = ",i)
	worker_id = i
	slots = int(input("enter number of slots: "))
	port = int(input("enter port no: "))
	dictionary = {"worker_id": worker_id,"slots": slots,"port": port}
	l.append(dictionary)
d = {"workers": l}
with open("vvv.json","w") as output:
	json.dump(d,output)
