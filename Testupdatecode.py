target_ip = "10.10.100.1"
begins = "Nmap scan report for"

fhand = open('ScanTest.txt','r')
for line in fhand:
    line = line.rstrip()
    if line.startswith(begins) and line.endswith(target_ip):
        print(line)