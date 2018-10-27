#!
#Python3.7.x


#modules 
import linecache


#variables
report=input('Name of the file of Nmap Scan:\n')
target_ip=input('Which target is the report needed on?:\n')
begins = "Nmap scan report for"
fhand = open(report,'r')
beginsend = "\n"



#This information is to get the line number for our first line.
for num1,line1 in enumerate(fhand, 1):
    line1 = line1.rstrip()
    if line1.startswith(begins) and line1.endswith(target_ip):
        #print(num1)
        #print(line1)
        break
# This part is to get the line number for our end of the report   
for num2,line2 in enumerate(fhand, 1):
    
    if line2.startswith(beginsend):
        #print(num2)
        #print(line2)
        break
#this will index the report and print a range from num1 to num1+num2    
with open(report) as f:
    linecount = sum(1 for line in f)
    
for i in range(num1,num1+num2):
    
    print(linecache.getline(report, i))