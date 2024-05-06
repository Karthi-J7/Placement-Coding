# Longest Substring with Unique Characters

s = input()
n = len(s)
max_length = 0
substring = ""

for i in range(n):
    for j in range(i + 1, n):
        temp = s[i : j]
        if len(set(temp)) > max_length:
            substring = temp
            max_length = len(set(temp))

print(substring)
