import nmap

target = "example.com"  #here i used example.com as a target but u can use ur own

scanner = nmap.PortScanner()
scanner.scan(target, '1-65535')  #Scan all ports from 1 to 65535

for port in scanner[target]['tcp']:
    if scanner[target]['tcp'][port]['state'] == 'open':
        print(f"Port {port} is open")
