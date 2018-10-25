import linecache

report = "ScanTest.txt"
target_ip = "10.10.100.2"
begins = "Nmap scan report for"
fhand = open(report,'r')
beginsend = "Network Distance:"





for num1,line1 in open(fhand, 1):
    linecount = sum(1 for line in fhand)
    if line1.startswith(begins) and line1.endswith(target_ip):
        print(num1)
    
for i in range(2,24):
    
    print(linecache.getline("ScanTest.txt", i))