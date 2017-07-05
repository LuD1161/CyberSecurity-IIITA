import socket
import threading
from Queue import Queue
import time
import json 

print_lock = threading.Lock()
target = "127.0.0.1"

with open('blacklist.json') as x:
	blacklist=json.load(x)


dictionary={}
i=0
def portscan(port):
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		con=s.connect((target,port))
        	k=port
        	global i
        	i=i+1
        	dictionary[i]={}
        	try:
        		dictionary[i]['port']=str(k)
        		dictionary[i]['type_of_port']=str(blacklist[str(k)]['type'])
        		dictionary[i]['remarks']=str(blacklist[str(k)]['service'])
        		
        	except:
        		 dictionary[i]['port']=str(k)
        		 dictionary[i]['remarks']="not in blacklisted ports"
        	con.close()
        except:
             pass
def threader():
	while True:
        	worker = q.get()
                portscan(worker)
                q.task_done()
 
q=Queue()
 
for x in range(40):
 	t=threading.Thread(target=threader)
        t.daemon = True
        t.start()
       
for worker in range(1,65000):
	q.put(worker)
	
with open('output.json','aw') as output:
	json.dump(dictionary, output, ensure_ascii=False,indent=4)
q.join()

    

