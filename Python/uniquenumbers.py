l = [int(i) for i in input().split()]
n = len(l)
l.sort()

print(l[0])
for i in range(1, len(l)):
    if not (l[i] == l[i - 1]):
        print(l[i])