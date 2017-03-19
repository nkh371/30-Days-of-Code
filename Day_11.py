ar = []
for i in range(6):
    arr = map(int,raw_input().strip().split(' '))
    ar.append(arr)
max1 = -50
for i in range(4):
    for j in range(4):
        sum1 = 0
        for k in range(0 + i,3 + i):
            for l in range(0 + j,3 + j):
                if k == 1 + i:
                    if l  != 1 + j:
                        continue
                sum1 += ar[k][l]
        if max1 < sum1:
            max1 = sum1    
print max1
