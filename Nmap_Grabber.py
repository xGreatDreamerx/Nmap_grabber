#Python3.7.x
#
#
import linecache
#report=input('Name of the file of Nmap Scan:\n')
#target_ip=input('Which target is the report needed on?:\n')

report = "ScanTest.txt"
target_ip = "10.10.100.2"
begins = "Nmap scan report for"
fhand = open(report,'r')
beginsend = "Network Distance:"

for num1,line1 in enumerate(fhand, 1):
    line1 = line1.rstrip()
    if line1.startswith(begins) and line1.endswith(target_ip):
        print(num1)
        print(line1)
        break
for num2,line2 in enumerate(fhand, 1):
    line2 = line2.rstrip()
    if line2.startswith(beginsend) and num2 > num1:
        print(num2)
        print(line2)
        break
with open('ScanTest.txt') as f:
    linecount = sum(1 for line in f)
    
for i in range(num1,num2):
    
    print(linecache.getline("ScanTest.txt", i))