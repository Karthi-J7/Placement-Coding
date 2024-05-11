n = input()


if len(n) < 2:
    print("Minimum Required digits : 2") 
temp = 0

while int(n) > 9:
    temp = ''
    for i in range(len(n) - 1):
        temp = abs(int(n[i]) - int(n[i]))    
    n = temp

print(n)
