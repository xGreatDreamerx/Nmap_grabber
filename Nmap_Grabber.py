#
#
#
#
report=input('Name of the file of Nmap Scan:\n')
target_ip=input('Which target is the report needed on?:\n')


target_ip = "10.10.100.1"
begins = "Nmap scan report for"

fhand = open(report,'r')
for line in fhand:
    line = line.rstrip()
    if line.startswith(begins) and line.endswith(target_ip):
        print(line)
        
           