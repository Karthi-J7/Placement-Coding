l = [int(i) for i in input().split()]
n = len(l)

max = 0
smax = -1

for i in range(n):
    if max < l[i]:
        smax = max
        max = l[i]
    
    elif smax < l[i] < max:
        smax = l[i]

print(smax)