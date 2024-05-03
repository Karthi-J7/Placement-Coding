n = input()


if len(n) < 2:
    print("Minimum Required digits : 2") 
temp = 0

while int(n) > 9:
    temp = 0
    for i in n:
        temp = abs(int(i) - temp)
    
    n = temp

print(n)
