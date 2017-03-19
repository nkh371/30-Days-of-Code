from __future__ import print_function

t = int(raw_input())
for i in range(0,t):
    ar = str(raw_input())
    n = len(ar)
    for j in range(0,n,2):
        print (ar[j],end = '')
    print (' ',end = '')
    for j in range(1,n,2):
        print (ar[j],end = '')
    print ('\n',end = '')
