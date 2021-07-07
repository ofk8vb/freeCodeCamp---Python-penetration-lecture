import nmap

scanner = nmap.PortScanner()


print('Welcome, this is a simple nmap automation tool')
print('<----------------------------------------------------->')

ip_addr = input('Please enter the IP Address you want to scan: ')
print('The IP you entered is: ', ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1->SYN ACK Scan
                2->UDP Scan
                3->Comprehensive Scan \n""")
print('You have selected option: ',resp)

if resp == '1':
    print('Nmap version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS') # second argument is range of ports to scan for, third argument is verbose logging, and SYNACK scan
    print(scanner.scaninfo())
    print('Ip Status: ', scanner[ip_addr].state) # whether ip is online or offline
    print(scanner[ip_addr].all_protocols())
    print('Open Ports: ', scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print('Nmap version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU') # second argument is range of ports to scan for, third argument is verbose logging, and SYNACK scan
    print(scanner.scaninfo())
    print('Ip Status: ', scanner[ip_addr].state) # whether ip is online or offline
    print(scanner[ip_addr].all_protocols())
    print('Open Ports: ', scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print('Nmap version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O') # second argument is range of ports to scan for, third argument is verbose logging, and SYNACK scan
    print(scanner.scaninfo())
    print('Ip Status: ', scanner[ip_addr].state) # whether ip is online or offline
    print(scanner[ip_addr].all_protocols())
    print('Open Ports: ', scanner[ip_addr]['tcp'].keys())
elif resp >=4:
    print('Please enter a valid option')