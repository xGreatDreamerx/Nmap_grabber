#Python3.7.x
#
#
import linecache
#report=input('Name of the file of Nmap Scan:\n')
#target_ip=input('Which target is the report needed on?:\n')

report = "ScanTest.txt"
target_ip = "10.10.100.1"
begins = "Nmap scan report for"
fhand = open(report,'r')
beginsend = "\n"

for num1,line1 in enumerate(fhand, 1):
    line1 = line1.rstrip()
    if line1.startswith(begins) and line1.endswith(target_ip):
        #print(num1)
        #print(line1)
        break
for num2,line2 in enumerate(fhand, 1):
    
    if line2.startswith(beginsend):
        #print(num2)
        #print(line2)
        break
with open('ScanTest.txt') as f:
    linecount = sum(1 for line in f)
    
for i in range(num1,num1+num2):
    
    print(linecache.getline("ScanTest.txt", i))