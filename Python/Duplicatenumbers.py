l = [int(i) for i in input().split()]
n = len(l)
l.sort()
t = 0

for i in range(n - 1):
    if l[i] == l[i + 1] and t != l[i]:
        t = l[i]
        print(t)
