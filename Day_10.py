n = int(raw_input())
max_ = 0
c = 0
while n:
    if n & 1:
        c += 1
        if max_ < c:
            max_ = c
    else:
        c = 0
    n = n/2
print max_
