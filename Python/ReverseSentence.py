s = input()
reversed_sentence = ''

for i in s:
  if i == '':
    s += ''
  else:
    s += i

print(s)
