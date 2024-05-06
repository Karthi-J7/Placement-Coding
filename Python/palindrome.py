# palindrome program using two pointer 

s = input().lower()
start, end = 0, len(s) - 1
key = True

while start <= end:
    if s[start] != s[end]:
        key = False
        break
    start += 1
    end -= 1

print(f'{s} is {"a" if key else "not a"} palindrome')