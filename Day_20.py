n = int(raw_input())
ar = map(int,raw_input().split(' '))
c = 0
for i in range(0, n - 1):
    d = 0
    for j in range(0, n- i - 1):
        if ar[j] > ar[j+1]:
            t = ar[j]
            ar[j] = ar[j+1]
            ar[j+1] = t
            d = 1
            c += 1
    if d != 1:
        break
        
print 'Array is sorted in',c,'swaps.'
print 'First Element:',ar[0]
print 'Last Element:',ar[n-1]
