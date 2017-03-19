n = int(raw_input())
ar = {}
for i in range(0,n):
    data = raw_input().split(' ')
    ar[data[0]] = data[1]
while 1:
    d = str(raw_input())
    if d == None:
        break
    if d in ar:
        print d + '=' + ar[d]
    else:
        print 'Not found'
