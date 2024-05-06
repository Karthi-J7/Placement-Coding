s = input()
reversed_sentence = ''
temp = ''


for i in s:
  if i == ' ':
    reversed_sentence = i + temp + reversed_sentence
    temp = ''
  else:
    temp += i

reversed_sentence = temp + reversed_sentence

print(reversed_sentence)
