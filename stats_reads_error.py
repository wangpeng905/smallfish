#!/usr/bin/env python2

input_fa = open(sys.argv[1],'r')
refseq = "AGTGGGCGTAGGACGATGA..........."

error_dict = {}
for i in range(100):
    error_dict[i] = 0

reads_num = 0

for line in input_fa:
    if line.startswith(">"):
        reads_num += 1
    else:
        line = line.strip()
        base_num = 0
        while base_num < 100:
            if line[base_num] == refseq[base_num]:
                pass
            else:
                error_dict[base_num] += 1
            base_num += 1

for k in range(100):
    print "The %dth base has %d errors!"%(k+1,error_dict[k])

print "total reads number:",reads_num