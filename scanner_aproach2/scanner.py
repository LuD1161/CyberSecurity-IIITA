#!/usr/bin/python
# coding: utf-8

import json
import socket
import threading
from Queue import Queue

print_lock = threading.Lock()
target = '127.0.0.1'
with open('blacklist.json') as x:
    blacklist = json.load(x)
    
try:
	with open('output.json') as check:
		checklist=json.load(check)	
except:
	checklist={}
	
dictionary = {}
list = []

def portscanudp (port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
    	global checklist
        con = s.connect((target, port))
        k=0
        for i in checklist:
        	if str(port)==checklist[i]['port']:
        		k=1
               		x = str(port) + ",," + str(socket.getservbyport(port, 'udp'))+",,"+'udp'+",,"+'old'
        if(k==0):
        	x = str(port) + ',,' + str(socket.getservbyport(port, 'udp')) + ',,' + 'udp'+",,"+'new'
        list.append(x)
        con.close()
    except:
        pass


def portscantcp (port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
    	global checklist
        con = s.connect((target, port))
        try:
        	m=0
        	for i in checklist:
        		if str(port)==checklist[i]['port']:
        			m=1
        			x = str(port) + ',,' + str(socket.getservbyport(port, 'tcp')) + ',,' + 'tcp'+",,"+'old'
        	if(m==0):
        		x = str(port) + ',,' + str(socket.getservbyport(port, 'tcp')) + ',,' + 'tcp'+",,"+'new'
        		
                list.append(x)
        except:
        	n=0
        	for i in checklist:
        		if str(port)==checklist[i]['port']:
        			n=1
            			x = str(port) + ',,' + 'SERVICE_NOT_FOUND' + ',,' + 'tcp'+",,"+'old'
            	if n==0:
            		x = str(port) + ',,' + 'SERVICE_NOT_FOUND' + ',,' + 'tcp'+",,"+'new'
            		
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
    try:
        if blacklist[list[i]]:
            try:
                dictionary[i + 1]['port'] = str(small_list[0])
                dictionary[i + 1]['type of port'] = str(small_list[2])
                dictionary[i + 1]['service'] = str(small_list[1])
                dictionary[i + 1]['remarks'] = blacklist[list[i]]
                dictionary[i + 1]['new_or_old'] = str(small_list[3])
            except:
                pass
    except:
        dictionary[i + 1]['port'] = str(small_list[0])
        dictionary[i + 1]['remarks'] = 'not in blacklisted ports'
        dictionary[i + 1]['service'] = str(small_list[1])
        dictionary[i + 1]['type of port'] = str(small_list[2])
        dictionary[i + 1]['new_or_old'] = str(small_list[3])

with open('output.json','w') as x:
	json.dump(dictionary,x,ensure_ascii=False,indent=8)
