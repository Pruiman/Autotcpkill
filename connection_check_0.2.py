#!/usr/bin/python
import os, sys, time
n = []
c = []
for i1 in range(10):
    for i2 in range(10):
        for i3 in range(10):
            if i1==0 and i2==0 and i3!=0:
                c.append(str(i3))
            elif i1==0 and i2!=0:
                c.append(str(i1)+str(i2))
            elif i1!=0:
                c.append(str(i1)+str(i2)+str(i3))
while True:
    command = "arp>buffer.txt"
    result = os.system(command)
    with open('buffer.txt', 'r') as f:
        result = f.read()
        print(result)
    with open(r"buffer.txt", 'r') as fil:
        for line in fil:
            for i in range(len(c)):
                if "_gateway" in line:
                    continue
                elif c[i] in line:
                    n.append(line[:-1])
    tark = len(n)
    n.append(" ")
    for jerg1 in range(tark):
        if n[jerg1]==" ":
            continue
        else:
            while n.count(n[jerg1])>1:
                del n[jerg1]
                n.append(" ")
    while " " in n:
        n.remove(" ")
    nl = []
    for jergo in range(len(n)):
        t = n[jergo]
        t = t.split()
        nl += t
    for jergo1 in range(1,len(nl),5):
        nl[jergo1] = " "
    for jergo2 in range(2,len(nl),5):
        nl[jergo2] = " "
    for jergo3 in range(3,len(nl),5):
        nl[jergo3] = " "
    while " " in nl:
        nl.remove(" ")
    nt1 = []
    for jarm1 in range(0,len(nl),2):
        t = nl[jarm1]
        nt1.append(t)
    print(nt1)
    nt2 = []
    for jarm2 in range(1,len(nl),2):
        t = nl[jarm2]
        nt2.append(t)
    r = []
    with open(r"whitelist.txt",'r') as file1:
        for line in file1:
            r.append(line)
    for tax in range(len(r)):
        r[tax] = r[tax][:-1]
    for tars in range(len(nt1)):
    	if nt1[tars] not in r:
    	    com = "tcpkill -i " + nt2[tars] + " host " + nt1[tars] + " & python connection_check_0.2.py"
    	    os.system(com)
    	else:
    	    continue
    time.sleep(10)
