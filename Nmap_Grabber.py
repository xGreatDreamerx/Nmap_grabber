import pprint
pp = pprint.PrettyPrinter(indent=4)
report=input('Name of the file of Nmap Scan:\n')
target_ip=input('Which target is the report needed on\n')


with open(report,'r') as f:
    for line in f.readlines():
        # python can do regexes, but this is for s fixed string only
        if target_ip in line:
            idx1 = line.find('"')
            idx2 = line.find('"', idx1+1)
            field = line[idx1+1:idx2-1]
            pprint.pprint(field)
        
           