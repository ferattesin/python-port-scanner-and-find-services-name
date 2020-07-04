import socket
from threading import Thread
from queue import Queue

#sample port list 
port_list = [21,22,46,80,53,113,587,443,5454,32768,587,143]

scanned_port_list = Queue()

#sample target site
target = "target.com"

def port_scanner(port):

    while True:

        port_number = port.get()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            con = s.connect((target,port_number))
            port_services = socket.getservbyport(port_number, "tcp")
            print("port ",port_number," is open"," services: ", port_services,end="\n***************************************\n")  
            
            con.close()
      
        except:
            pass

        
        port.task_done()



for i in range(30):

    t = Thread(target=port_scanner, args = (scanned_port_list,))

    t.daemon = True

    t.start()



for x in port_list:

    scanned_port_list.put(x)    


scanned_port_list.join()
