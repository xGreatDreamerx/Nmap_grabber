#Python3.7.x
#
#
#
#report=input('Name of the file of Nmap Scan:\n')
#target_ip=input('Which target is the report needed on?:\n')
report = "ScanTest.txt"
target_ip = "10.10.100.2"
begins = "Nmap scan report for"
fhand = open(report)
beginsend = "Network Distance:"
 
with fhand as file_txt:
    
    for num1,line1 in enumerate(fhand, 1):
        line1 = line1.rstrip()
        if line1.startswith(begins) and line1.endswith(target_ip):
        
            print(num1,line1)
            break
    for num2,line2 in enumerate(fhand, 1):
        if line2.startswith('\n') and num2 > num1 :
        
            print(num2,line2)
            #print(line)
            #print(num1,line1,'\n',num2,line2)    
            break
print(num1 , num2)
