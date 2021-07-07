import socket


def banner(ip, port):
    s = socket.socket()
    s.connect((ip,int(port)))
    s.settimeout(5) # if no response is given in 5 seconds drop
    print(s.recv(1024)).strip('b') # get rid of anything with b (to demonstrate a feature)

def main():
    ip = input('Please enter the IP: ')
    port = str(input('Please enter the port: '))
    banner(ip, port)

main()

