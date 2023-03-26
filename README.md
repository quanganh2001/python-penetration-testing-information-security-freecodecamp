Here is my full source code about Python for Penetration Testing:
# Creating a TCP Server
```py
#!/usr/bin/python3

import socket

# Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '192.168.1.107'
host = socket.gethostname()
port = 444

# Binding to socket
serversocket.bind(('192.168.1.107', port)) # host will be replaced/substituted with IP, if changed and not running on host

# Starting TCP listener
serversocket.listen(3)

while True:
    # Starting the connection
    clientsocket, address = serversocket.accept()
    
    print("received connection from %s " % str(address))
    
    message = 'Hello! Thank you for connecting to the server' + "\r\n"
    
    clientsocket.send(message.encode('ascii'))
    
    clientsocket.close()

```
# Creating a TCP Client
```py
#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '192.168.1.107'
host = socket.gethostname()

port = 444

clientsocket.connect(('192.168.1.107', port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
```

Note: please run client python on your virtual machine to see output TCP Server.

# Developing an Nmap Scanner
```py
#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<-------------------------------------------->")

ip_addr = input("Please enter IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
				1) SYN ACK Scan
                2) UDP Scan
                3) Comprehension Scan \n""")
print("You have selected the option: ", resp)

if resp == '1':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp >= '4':
    print("Please enter a valid option")
```

Before run this code, please following the requirements:

1. Type `pip3 install python-nmap`
2. Type `sudo apt-get install nmap`

If you try to type sudo python3 Scanner.py, it was error:
```txt
Traceback (most recent call last):
  File "/home/quanganh/Desktop/Scanner.py", line 3, in <module>
    import nmap
ModuleNotFoundError: No module named 'nmap'
```

The error message suggests that the Python interpreter cannot find the nmap module even though you have installed it using pip.

This could be due to the fact that you installed the module using pip for your user account, but you are running the script with root privileges using sudo. When you run a command with sudo, it runs with the environment variables and file paths of the root user, which may be different from your user account.

To fix this error, you can try installing the nmap module for the root user. You can do this by running the following command: `sudo pip3 install python-nmap`

This should install the nmap module system-wide, making it available to all users, including the root user. Once the module is installed, you can try running your script with sudo again: `sudo python3 Scanner.py` 

If you still encounter the error, you can try specifying the full path to the Python interpreter that has the nmap module installed, like this: `sudo /usr/bin/python3 Scanner.py`

This should ensure that the script runs with the correct Python interpreter and has access to the nmap module.

Output:
```txt
Welcome, this is a simple nmap automation tool
<-------------------------------------------->
Please enter IP address you want to scan: 192.168.1.107
The IP you entered is:  192.168.1.107

Please enter the type of scan you want to run
				1) SYN ACK Scan
                2) UDP Scan
                3) Comprehension Scan 
1
You have selected the option:  1
Nmap Version:  (7, 80)
{'tcp': {'method': 'syn', 'services': '1-1024'}}
Ip Status:  up
['tcp']
Open Ports:  dict_keys([444, 902, 912])

Welcome, this is a simple nmap automation tool
<-------------------------------------------->
Please enter IP address you want to scan: 192.168.1.107
The IP you entered is:  192.168.1.107

Please enter the type of scan you want to run
				1) SYN ACK Scan
                2) UDP Scan
                3) Comprehension Scan 
2
You have selected the option:  2
Nmap Version:  (7, 80)
{'udp': {'method': 'udp', 'services': '1-1024'}}
Ip Status:  up
['udp']
Open Ports:  dict_keys([137])

Welcome, this is a simple nmap automation tool
<-------------------------------------------->
Please enter IP address you want to scan: 192.168.1.107
The IP you entered is:  192.168.1.107

Please enter the type of scan you want to run
				1) SYN ACK Scan
                2) UDP Scan
                3) Comprehension Scan 
3
You have selected the option:  3
Nmap Version:  (7, 80)
{'tcp': {'method': 'syn', 'services': '1-1024'}}
Ip Status:  up
['tcp']
Open Ports:  dict_keys([444, 902, 912])
```
# Developing a Banner Grabber
```py
#!/usr/bin/python3

import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    print(str(s.recv(1024)).strip('b'))

def main():
    ip = input("Please enter the IP: ")
    port = str(input("Please enter the port: "))
    banner(ip, port)

main()
```
*Note: Please still run TCP Server.*

Output:
```txt
Please enter the IP: 192.168.1.107
Please enter the port: 444
'Hello! Thank you for connecting to the server\r\n'
```
# Developing a Port Scanner
```py
#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan: "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)
```
Output:
```txt
Please enter the IP you want to scan: 192.168.1.107
Please enter the port you want to scan: 444
The port is open
```
