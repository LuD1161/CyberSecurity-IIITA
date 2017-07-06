#!/usr/bin/env python
import json
import socket
import threading
from Queue import Queue
print_lock = threading.Lock()
target = "127.0.0.1"
with open('blacklist.json') as x:
    blacklist = json.load(x)
dictionary = {}
NewlyOpendPorts = {}
list = []
portnew = []
portold = []
def new():
    with open('output.json') as x:
        data = json.load(x)
    for i in (data):
        if "ports" in data[i]:
            portold.append(data[i]["ports"])
new()
def portscanudp (port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        con = s.connect((target, port))
        x = str(port) + ",," + str(socket.getservbyport(port, 'udp')) + ",," + 'udp'
        list.append(x)
        con.close()
    except:
        pass
def portscantcp (port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        try:
            x = str(port) + ",," + str(socket.getservbyport(port, 'tcp')) + ",," + 'tcp'
            list.append(x)
        except:
            x = str(port) + ",," + "SERVICE_NOT_FOUND" + ",," + 'tcp'
            list.append(x)
        con.close()
    except:
        pass
def threader ():
    while True:
        worker = q.get()
        portscanudp(worker)
        portscantcp(worker)
        q.task_done()
q = Queue()
for x in range(40):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()
for worker in range(1, 65535):
    q.put(worker)
q.join()
for i in range(len(list)):
    dictionary[i + 1] = {}
    small_list = list[i].split(',,')
    portnew.append(str(small_list[0]))
    try:
        if blacklist[list[i]]:
            try:
                dictionary[i + 1]['ports'] = str(small_list[0])
                dictionary[i + 1]['type of port'] = str(small_list[2])
                dictionary[i + 1]['service'] = str(small_list[1])
                dictionary[i + 1]['remarks'] =  blacklist[list[i]]
            except:
                pass
    except:
        dictionary[i + 1]['ports'] = str(small_list[0])
        dictionary[i + 1]['remarks'] = 'not in blacklisted ports'
        dictionary[i + 1]['service'] = str(small_list[1])
        dictionary[i + 1]['type of port'] = str(small_list[2])
for i in (set(portnew)-set(portold)):
    dictionary['NewlyOpen'] ={}
    dictionary['NewlyOpen'][i] ='NEW'
with open('output.json','w') as x:
	json.dump(dictionary,x,indent=8)